console.log("Hello, this is console.log");

console.info("This is console.info message");

console.warn("This is a warning message");

console.error("This is an error message");

console.debug("This is a debug message");

const students = [
  { id: 1, name: "Devi", course: "JavaScript" },
  { id: 2, name: "Chinni", course: "Python" }
];
console.table(students);

let age = 17;
console.assert(age >= 18, "Age must be 18 or above");

console.count("Button clicked");
console.count("Button clicked");

console.countReset("Button clicked");

console.group("User Details");
console.log("Name: Devi");
console.log("Role: Student");
console.groupEnd();

console.groupCollapsed("Collapsed Group");
console.log("Hidden message 1");
console.log("Hidden message 2");
console.groupEnd();

console.time("loopTime");
for (let i = 0; i < 100000; i++) {}
console.timeEnd("loopTime");

function first() {
  second();
}
function second() {
  console.trace("Trace function call");
}
first();

const person = { name: "Devi", age: 22, skills: ["JS", "Python"] };
console.dir(person);

console.dirxml(document.body);

console.time("process");
console.timeLog("process");
console.timeEnd("process");

console.log("My name is %s and age is %d", "Devi", 22);

console.log("%cStyled Text", "color: green; font-size: 20px; font-weight: bold;");