CREATE TABLE `User` (
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `email` TEXT NOT NULL,
    `password` TEXT NOT NULL,
    `firstName` TEXT NOT NULL,
    `lastName` TEXT NOT NULL,
    `displayName` TEXT NOT NULL,
    `photo` TEXT,
    `profileCreation` INTEGER NOT NULL,
    `profileType` TEXT NOT NULL
);


DROP TABLE 'Tag'
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


INSERT INTO `User` VALUES (null, "Madi@Madi.com", "password", "Madi", "Peper", "","", 1601234567890, "Admin");
INSERT INTO `User` VALUES (null, "Pete@Pete.com", "password", "Peter", "Pickles", "","", 1601234567890, "Admin");
INSERT INTO `User` VALUES (null, "Bradly@Bradly.com", "password", "Bradly", "Braderson", "","", 1601234567890, "Admin");





INSERT INTO `Tag` VALUES (null, 'tag title');
INSERT INTO `Tag` VALUES (null, 'tag title');
INSERT INTO `Tag` VALUES (null, 'tag title');



INSERT INTO `Comment` VALUES (null, "comment body", 1, 2);
INSERT INTO `Comment` VALUES (null, "coment body", 1, 2);
INSERT INTO `Comment` VALUES (null, "comment body", 1, 2);



INSERT INTO `Post` VALUES (null, "Title", "Stuff", 2, 4, 1);
INSERT INTO `Post` VALUES (null, "Title", "things", 2, 1, 1);
INSERT INTO `Post` VALUES (null, "Title", "Things", 2, 4, 2);


INSERT INTO `Posttag` VALUES (null, 3, 1);
INSERT INTO `Posttag` VALUES (null, 1, 1);
INSERT INTO `Posttag` VALUES (null, 3, 2);



INSERT INTO `Category` VALUES (null, "Programming");
INSERT INTO `Category` VALUES (null, "Nature");
INSERT INTO `Category` VALUES (null, "Food");





SELECT * FROM Tag
SELECT * FROM Comment
SELECT * FROM Category
SELECT * FROM User
SELECT * FROM Post
SELECT * FROM Posttag

