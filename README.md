> This project is unmaintained.
>
> It should not be run exposed to the Internet or placed behind a secure
> reverse proxy with authentication in front.
>
> All versions are pinned so that the `Dockerfile` should build. For a
> working example please see `docker-compose.yml`.
>
> Graphs cannot be imported via the user interface.
> However the database can be backed up
> (`docker compose exec ore-db pg_dump -U ore -d ore > backup.sql`)
> and restored
> (`docker-compose exec -T ore-db psql -U ore -d ore < backup.sql`).
> For this, make sure to remember your username.
> If the database is already used, it can be dropped by running
> `docker-compose exec ore-db dropdb -U ore ore` and recreated empty by
> running `docker-compose exec ore-db createdb -U ore ore`.

[![Build Status](https://travis-ci.org/troeger/fuzzed.svg?branch=master)](https://travis-ci.org/troeger/fuzzed)
[![Security Status](https://pyup.io/repos/github/troeger/fuzzed/shield.svg)]( https://pyup.io/repos/github/troeger/fuzzed/)
[![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/troeger/fuzzed/badges/quality-score.png?b=master)](https://scrutinizer-ci.com/g/troeger/fuzzed/?branch=master)

# ORE - The Open Reliability Editor (former FuzzEd)

Note: FuzzEd becomes ORE. We are in the middle of that process, so don't get confused while both names are still in use.

ORE is an browser-based editor for drawing and analyzing dependability models. The currently supported types are:

* Fault Tree Diagrams
* FuzzTree Diagrams
* Reliability Block Diagrams
* Data Flow Diagrams

The editor supports the following generic features for all diagram types:

* Organization of diagrams in projects, per user.
* Sharing of (read-only) graphs between users of the same installation. We use that heavily for education scenarios.
* Creation of diagram snapshots.
* Full clipboard functionality inside the editor.
* LaTEX, PDF and EPS export for some diagram types.
* GraphML export for all diagram types.
* Analytical and simulation-based analysis of fault tree and FuzzTree diagrams. 
* REST API for creating new diagrams with external software.

You can try the editor at https://live.ore-project.org.

## Production Deployment

The latest release of ORE is available on Docker Hub. 

## Development

Thanks for your interest in this project. We would love to have you on-board. The developers discuss in the [ORE forum](https://groups.google.com/forum/#!forum/ore-dev).

The only supported environment for development is Docker Compose.

Get a checkout and run:

``make dev-build``

This prepares docker images for the frontend and the backend part and compiles neccessary code parts inside the containers.

Now run:

``make dev-up``

This starts the images and runs the frontend Django development server, the backend daemon and the database in separate containers. You should now be able to use the frontend on your machine at http://localhost:8000. The start page has a *Developer Login* link right below the OAuth login logos, which works without Internet connectivity.  The OAuth login logos are broken by default, since you need [OAuth2 credentials](https://github.com/troeger/fuzzed/wiki/OAuth2Cred) to be configured for that.

If your working on a staging machine, a valid option is to get an OpenID from somewhere such as https://openid.stackexchange.com.

## Licence

ORE ist licensed under the [GNU AGPL Version 3](http://en.wikipedia.org/wiki/Affero_General_Public_License). This means your are allowed to:

* Install and run the unmodified ORE code at your site.
* Re-package and distribute the unmodified version of ORE from this repository. 
* Fork and re-publish the editor, as long as your modified sources are accessible for everybody.

In short, AGPL forbids you to distribute or run your own modified version of ORE without publishing your code.
 
## Acknowledgements

People who contributed to this project so far:

* Franz Becker      (analysis)
* Markus Götz       (core architecture, frontend)
* Lena Herscheid    (analysis, simulation)
* Felix Kubicek     (frontend)
* Stefan Richter    (frontend)
* Frank Schlegel    (core architecture, frontend)
* Christian Werling (frontend)
