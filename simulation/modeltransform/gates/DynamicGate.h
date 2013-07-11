#pragma once
#include "Gate.h"
#include <assert.h>

class DynamicGate : public Gate
{
public:
	DynamicGate(const std::string& ID, const std::string& name) : Gate(ID, name) {}
	virtual ~DynamicGate() {}

	bool isDynamic() const { return true; }
	virtual std::string serializeAsFormula(boost::shared_ptr<PNDocument> doc) const override { assert(false); return ""; }
};