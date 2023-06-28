const airline = "TAP Air Portugal";
const plane = "A320";

console.log(airline.length);
console.log("B737"[0]);

// getting index
console.log("\n\tindex\n\t------");
console.log(airline.indexOf("r"));
console.log(airline.lastIndexOf("r"));
console.log(airline.indexOf("lap")); // -1: not found

// slice: extract the parts of the string
console.log("\n\tSlice\n\t------");
console.log(airline.slice(4)); // returns a new string
console.log(airline.slice(4, 7)); // the last index is exclusive

console.log(airline.slice(0, airline.indexOf(" "))); // get the first word
console.log(airline.slice(airline.lastIndexOf(" ") + 1)); // get the last word

const checkMiddleSeat = function (seat) {
  const s = seat.slice(-1);
  if (s === "B" || s === "E") console.log("You got the middle seat.");
  else console.log("You got lucky");
};

checkMiddleSeat("11B");
checkMiddleSeat("23C");

// boxing: JS takes string primitives and convert them into string objects on which all the above methods are called
console.log("\n\tBoxing\n\t------");
console.log(new String("La paix"));
console.log(typeof new String("La paix")); // check the type

// capitalisation
console.log("\n\tCases\n\t------");
console.log(airline.toLowerCase());

const capitalizeName = function (theName) {
  let thenameLower = theName.toLowerCase();
  let theNameCorrected = thenameLower[0].toUpperCase() + thenameLower.slice(1);
  return theNameCorrected;
};

console.log(capitalizeName("la PaiX"));

// replacing
const priceGB = "288,97$";
console.log(priceGB.replace(",", "."));

console.log("\n\tReplace\n\t------");
const announcement =
  "All passengers come to boarding door 23. Boarding door 23!";
console.log(announcement.replace("door", "gate")); // replace first 'door' with 'gate'

console.log(announcement.replace(/door/g, "gate"));

// Booleans
console.log("\n\tBooleans\n\t------");

const plane2 = "Airbus A320neo";
console.log(plane2.includes("A320"));
console.log(plane2.includes("Boeing"));
console.log(plane2.startsWith("Airb"));

// split
console.log("\n\tSplit\n\t------");
const [fname, lname] = "Lapaix Gersh".split(" ");
console.log(lname);

const newName = ["Mr.", fname.toUpperCase(), lname].join(" ");
console.log(newName);

// capitalize 2
const capitalizeName2 = function (theName) {
  const names = theName.split(" ");

  const namesUpper = [];
  for (const name of names) {
    namesUpper.push(name[0].toUpperCase() + name.slice(1));
    //alternate: namesUpper.push(name.replace(name[0], name[0].toUpperCase()));
  }
  return namesUpper.join(" ");
};
const passenger3 = "jessica ann smith davis";
console.log(capitalizeName2(passenger3));

// padstart
console.log("\n\tPadstart\n\t------");
const phoneNum = "783563829";
console.log(phoneNum.padStart(14, "+250 "));

const maskCreditCard = function (number) {
  const str = number + "";
  const last = str.slice(-4);
  return last.padStart(str.length, "*");
};

console.log(maskCreditCard(32098764294));