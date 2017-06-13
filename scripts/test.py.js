/* This file was generated with PyCow - the Python to JavaScript translator */

var test_uds = new_class({

	initialize: function (test_case) {
		if (!isdefined(test_case)) test_case = "read_errcode";
		this.test_case = test_case;
	},

	print_case: function () {
		dbgprint(this.test_case);
	}
});

var main = function () {
	var T = new test_uds();
	/* Warning: Cannot infer type of -> */ T.print_case();
	dbgprint("%d--%d".sprintf(13, 14));
	return "%d--%d".sprintf(13, 14);
};

var fun = function (v1, v2) {
	var list_init = [1, 2, 3, 56];
	for (var __iter0_ = new _Iterator(tuple_init); __iter0_.hasNext();) {
		var x = __iter0_.next();
		dbgprint(x);
	}
	delete __iter0_;
	for (var __iter0_ = new _Iterator(list_init); __iter0_.hasNext();) {
		var y = __iter0_.next();
		dbgprint(y);
	}
	delete __iter0_;
	return v1 * v2;
};

main();

