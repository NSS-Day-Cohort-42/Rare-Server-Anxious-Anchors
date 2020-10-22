CREATE TABLE `User` (
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `email` TEXT NOT NULL,
    `password` TEXT NOT NULL,
    `firstName` TEXT NOT NULL,
    `lastName` TEXT NOT NULL,
    `displayName` TEXT NOT NULL,
    `photo` TEXT,
    `profileCreation` TEXT NOT NULL,
    `profileType` TEXT NOT NULL
);

CREATE TABLE `Tag` (
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `name` TEXT NOT NULL
);

CREATE TABLE `Category` (
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `name` TEXT NOT NULL
);

CREATE TABLE `Comment` (
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `commentBody` TEXT NOT NULL,
    `userId` INTEGER NOT NULL,
    `postId` INTEGER NOT NULL,
    FOREIGN KEY(`userId`) REFERENCES `User`(`id`),
    FOREIGN KEY(`postId`) REFERENCES `Post`(`id`)
);

CREATE TABLE `Post` (
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `postBody` TEXT NOT NULL,
    `postDate` TEXT,
    `title` TEXT NOT NULL,
    `userId` INTEGER NOT NULL,
    `CategoryId` INTEGER NOT NULL,
    FOREIGN KEY(`userId`) REFERENCES `User`(`id`),
    FOREIGN KEY(`CategoryId`) REFERENCES `Category`(`id`)
);

CREATE TABLE `Posttag` (
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `postId` INTEGER NOT NULL,
    `tagId` INTEGER NOT NULL,
    FOREIGN KEY(`postId`) REFERENCES `Post`(`id`),
    FOREIGN KEY(`tagId`) REFERENCES `Tag`(`id`)
);





INSERT INTO `Tag` VALUES (null, 'Nashville North');
INSERT INTO `Tag` VALUES (null, 'Nashville North');
INSERT INTO `Tag` VALUES (null, 'Nashville North');


INSERT INTO `User` VALUES (null, "Madi Peper", "35498 Madison Ave", "Madi Peper", "35498 Madison Ave", "Madi Peper", "35498 Madison Ave", "Madi Peper", "Madi Peper");
INSERT INTO `User` VALUES (null, "Madi Peper", "35498 Madison Ave", "Madi Peper", "35498 Madison Ave", "Madi Peper", "35498 Madison Ave", "Madi Peper", "Madi Peper");
INSERT INTO `User` VALUES (null, "Madi Peper", "35498 Madison Ave", "Madi Peper", "35498 Madison Ave", "Madi Peper", "35498 Madison Ave", "Madi Peper", "Madi Peper");



INSERT INTO `Comment` VALUES (null, "Mo Silvera", 1, 2);
INSERT INTO `Comment` VALUES (null, "Bryan Nilsen", 1, 2);
INSERT INTO `Comment` VALUES (null, "Jenna Solis", 1, 2);



INSERT INTO `Post` VALUES (null, "Snickers", "Recreation", 2, 4, 1);
INSERT INTO `Post` VALUES (null, "Jax", "Treatment", 2, 1, 1);
INSERT INTO `Post` VALUES (null, "Falafel", "Treatment", 2, 4, 2);


INSERT INTO `Posttag` VALUES (null, 4, 1);
INSERT INTO `Posttag` VALUES (null, 1, 1);
INSERT INTO `Posttag` VALUES (null, 4, 2);



INSERT INTO `Category` VALUES (null, "Snickers");
INSERT INTO `Category` VALUES (null, "Jax");
INSERT INTO `Category` VALUES (null, "Falafel");





SELECT * FROM Tag
SELECT * FROM Comment
SELECT * FROM Category
SELECT * FROM User
SELECT * FROM Post
SELECT * FROM Posttag

