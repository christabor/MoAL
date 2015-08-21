var aNumber = 1;
var aString = '1';
// Weak comparisons -- 1st = value, 2nd = value and type
var boolval1 = aNumber == aString;
var boolval2 = aNumber === aString;

var truthy1 = !null;
var truthy2 = 1;
var truth = true;
var falsy = false === Boolean(null);
var booltype = typeof Boolean;
var boolfunc = typeof Boolean == typeof (function(){});

// Haha... wtf
process.stdout.write('Truthy: ' + String(truthy1 == truth == truthy2) + '\n');
process.stdout.write('Falsy is really truthsy: ' + String(falsy) + '\n');
process.stdout.write('Boolean `type`: ' + String(booltype) + '\n');
process.stdout.write('Boolean type is... func? ' + String(boolfunc) + '\n');
// Weak - allowing coercion of string and bool type!
process.stdout.write('Boolean comparison coercion: ' + String(boolval1) + '\n'); // true!
// Weak - allowing coercion of string and bool type!
process.stdout.write('Boolean comparison coercion 2: ' + String(boolval2) + '\n') // false; type coercion happens.
