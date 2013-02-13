define(['editor', 'faulttree/graph', 'menus', 'faulttree/config'],
function(Editor, FaulttreeGraph, Menus, FaulttreeConfig) {
    /**
     *  Package: Faulttree
     */

    /**
     *  Class: CutsetsMenu
     *    A menu for displaying a list of minimal cutsets calculated for the edited graph. The nodes that belong to
     *    a cutset become highlighted when hovering over the corresponding entry in the cutsets menu.
     *
     *  Extends: <Base::Menus::Menu>
     */
    var CutsetsMenu = Menus.Menu.extend({
        /**
         *  Group: Members
         *
         *  Properties:
         *    {Graph} _graph - <Base::Graph> instance for which the cutsets are calculated.
         */
        _graph: undefined,

        /**
         *  Group: Initialization
         */

        /**
         *  Constructor: init
         *    Sets up the menu.
         *
         *  Parameters:
         *    {Graph} graph - The <Base::Graph> instance for which the cutsets are calculated.
         */
        init: function(graph) {
            this._super();
            this._graph = graph;
        },

        /**
         *  Group: Actions
         */

        /**
         *  Method: show
         *    Display the given cutsets in the menu and make the menu visible.
         *
         *  Parameters:
         *    {Array} cutsets - A list of cutsets calculated by the backend.
         *
         *  Returns:
         *    This menu instance for chaining.
         */
        show: function(cutsets) {
            if (typeof cutsets === 'undefined') {
                this.container.show();
                return this;
            }

            var listElement = this.container.find('ul').empty();

            _.each(cutsets, function(cutset) {
                var nodeIDs = cutset['nodes'];
                var nodes = _.map(nodeIDs, function(id) {
                    return this._graph.getNodeById(id);
                }.bind(this));
                var nodeNames = _.map(nodes, function(node) {
                    return node.name;
                });

                // create list entry for the menu
                var entry = jQuery('<li><a href="#">' + nodeNames.join(', ') + '</a></li>');

                // highlight the corresponding nodes on hover
                entry.hover(
                    // in
                    function() {
                        var allNodes = this._graph.getNodes();
                        _.invoke(allNodes, 'disable');
                        _.invoke(nodes, 'highlight');
                    }.bind(this),

                    // out
                    function() {
                        var allNodes = this._graph.getNodes();
                        _.invoke(allNodes, 'enable');
                        _.invoke(nodes, 'unhighlight');
                    }.bind(this)
                );

                listElement.append(entry);
            }.bind(this));

            this._super();
            return this;
        },

        /**
         *  Group: Setup
         */

        /**
         *  Method: _setupContainer
         *    Sets up the DOM container element for this menu and appends it to the DOM.
         *
         *  Returns:
         *    A jQuery object of the container.
         */
        _setupContainer: function() {
            return jQuery(
                '<div id="' + FaulttreeConfig.IDs.CUTSETS_MENU + '" class="menu" header="Cutsets">\
                    <div class="menu-controls">\
                        <span class="menu-minimize"></span>\
                        <span class="menu-close"></span>\
                    </div>\
                    <ul class="nav-list unstyled"></ul>\
                </div>'
            ).appendTo(jQuery('#' + FaulttreeConfig.IDs.CONTENT));
        }
    });

    var ProbabilityMenu = Menus.Menu.extend({
        /**
         *  Group: Members
         *
         *  Properties:
         *    {<Job>}  _job  - <Job> instance of the backend job that is responsible for calculating the probability.
         */
        _job:  undefined,

        /**
         *  Group: Initialization
         */

        /**
         *  Constructor: init
         *    Sets up the menu.
         */
        init: function() {
            this._super();
        },

        /**
         *  Group: Actions
         */

        /**
         *  Method: show
         *    Display the given job status (and finally its result).
         *
         *  Parameters:
         *    {<Job>} job - The backend job that calculates the probability of the top event.
         *
         *  Returns:
         *    This menu instance for chaining.
         */
        show: function(job) {
            //TODO: display job status
            console.log(job);

            this._super();
            return this;
        },

        /**
         *  Group: Setup
         */

        /**
         *  Method: _setupContainer
         *    Sets up the DOM container element for this menu and appends it to the DOM.
         *
         *  Returns:
         *    A jQuery object of the container.
         */
        _setupContainer: function() {
            return jQuery(
                '<div id="' + FaulttreeConfig.IDs.PROBABILITY_MENU + '" class="menu" header="Probability of Top Event">\
                    <div class="menu-controls">\
                        <span class="menu-minimize"></span>\
                        <span class="menu-close"></span>\
                    </div>\
                </div>'
            ).appendTo(jQuery('#' + FaulttreeConfig.IDs.CONTENT));
        }


    })

    /**
     *  Class: FaultTreeEditor
     *    Faulttree-specific <Base::Editor> class. The fault tree editor distinguishes from the 'normal' editor by
     *    their ability to calculate minimal cutsets for the displayed graph.
     *
     *  Extends: <Base::Editor>
     */
    return Editor.extend({
        /**
         *  Group: Members
         *
         *  Properties:
         *    {<CutsetsMenu>}     cutsetsMenu     - The <CutsetsMenu> instance used to display the calculated minimal cutsets.
         *    {<ProbabilityMenu>} probabilityMenu - The <ProbabilityMenu> instance used to display the probability of the top event.
         */
        cutsetsMenu: undefined,
        probabilityMenu: undefined,

        /**
         *  Group: Initialization
         */

        /**
         *  Constructor: init
         *    Sets up the cutset and probability menus in addition to <Base::Editor::init>.
         *
         *  Parameters:
         *    {int} graphId - The ID of the graph that is going to be edited by this editor.
         */
        init: function(graphId) {
            this._super(graphId);

            this.cutsetsMenu = new CutsetsMenu();
            this.probabilityMenu = new ProbabilityMenu()

            this._setupCutsetsActionEntry()
                ._setupTobEventProbabilityActionEntry();
        },

        /**
         *  Group: Accessors
         */

        /**
         *  Method: getConfig
         *
         *  Returns:
         *    The <FaulttreeConfig> object.
         *
         *  See also:
         *    <Base::Editor::getConfig>
         */
        getConfig: function() {
            return FaulttreeConfig;
        },

        /**
         *  Method: getGraphClass
         *
         *  Returns:
         *    The <FaulttreeGraph> class.
         *
         *  See also:
         *    <Base::Editor::getGraphClass>
         */
        getGraphClass: function() {
            return FaulttreeGraph;
        },

        /**
         *  Group: Setup
         */

        /**
         *  Method: _setupCutsetsActionEntry
         *    Adds an entry to the actions navbar group for calculating the minimal cutsets for the edited graph.
         *
         *  Returns:
         *    This editor instance for chaining.
         */
        _setupCutsetsActionEntry: function() {
            var navbarActionsEntry = jQuery(
                '<li>' +
                    '<a id="' + this.config.IDs.NAVBAR_ACTION_CUTSETS + '" href="#">Calculate cutsets</a>' +
                '</li>');
            this._navbarActionsGroup.append(navbarActionsEntry);

            // register for clicks on the corresponding nav action
            navbarActionsEntry.click(function() {
                jQuery(document).trigger(this.config.Events.EDITOR_CALCULATE_CUTSETS, this.cutsetsMenu.show.bind(this.cutsetsMenu));
            }.bind(this));

            return this;
        },

        /**
         *  Method: _setupTobEventProbabilityActionEntry
         *    Adds an entry to the actions navbar group for calculating the probability of the top event.
         *    Clicking will issue an asynchronous backend call which returns a <Job> object that can be queried for
         *    the final result. The job object will be used to initialize the probability menu.
         *
         *  Returns:
         *    This editor instance for chaining.
         */
        _setupTobEventProbabilityActionEntry: function() {
            var navbarActionsEntry = jQuery(
                '<li>' +
                    '<a href="#">Calculate top event probability</a>' +
                '</li>');
            this._navbarActionsGroup.append(navbarActionsEntry);

            // register for clicks on the corresponding nav action
            navbarActionsEntry.click(function() {
                jQuery(document).trigger(
                    this.config.Events.EDITOR_CALCULATE_TOPEVENT_PROBABILITY,
                    this.probabilityMenu.show.bind(this.probabilityMenu)
                );
            }.bind(this));

            return this;
        }
    });
});
