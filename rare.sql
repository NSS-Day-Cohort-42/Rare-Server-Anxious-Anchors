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

INSERT INTO `Tag` VALUES (null, 'Favorite');
INSERT INTO `Tag` VALUES (null, 'Dog');
INSERT INTO `Tag` VALUES (null, 'Cat');
INSERT INTO `Tag` VALUES (null, 'Rain');
INSERT INTO `Tag` VALUES (null, 'Running');
INSERT INTO `Tag` VALUES (null, 'Cycling');
INSERT INTO `Tag` VALUES (null, 'Nature');
INSERT INTO `Tag` VALUES (null, 'Fashion');
INSERT INTO `Tag` VALUES (null, 'Sad');

DROP TABLE `Tag`;

CREATE TABLE `Category` (
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `name` TEXT NOT NULL
);

INSERT INTO `Category` VALUES (null, 'Fiction');
INSERT INTO `Category` VALUES (null, 'Non Fiction');
INSERT INTO `Category` VALUES (null, 'Biography');
INSERT INTO `Category` VALUES (null, 'Fable');
INSERT INTO `Category` VALUES (null, 'Poem');

DROP TABLE `Category`;


CREATE TABLE `Post` (
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `postBody` TEXT NOT NULL,
    `postDate` INT NOT NULL,
    `title` TEXT NOT NULL,
    `userId` INTEGER NOT NULL,
    `CategoryId` INTEGER NOT NULL,
    FOREIGN KEY(`userId`) REFERENCES `User`(`id`),
    FOREIGN KEY(`CategoryId`) REFERENCES `Category`(`id`)
);

INSERT INTO `Post` VALUES (null, "This is a post about nothing.  I'm basically just trying this out.", 1603380251006, "Post About Nothing", 2, 1);
INSERT INTO `Post` VALUES (null, "This is a post about something.  Although it's not really anything.", 1502380251006, "Post About Nothing", 1, 4);
INSERT INTO `Post` VALUES (null, "This is a post.", 1303380251006, "It's just a post", 2, 3);
INSERT INTO `Post` VALUES (null, "I like dogs.", 1403380251006, "Post About Dogs", 1, 2);

DROP TABLE `Post`;


CREATE TABLE `Comment` (
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `commentBody` TEXT NOT NULL,
    `userId` INTEGER NOT NULL,
    `postId` INTEGER NOT NULL,
    FOREIGN KEY(`userId`) REFERENCES `User`(`id`),
    FOREIGN KEY(`postId`) REFERENCES `Post`(`id`)
);

INSERT INTO `Comment` VALUES (null, "Hi this is a test comment.  I wonder if it's going to work", 1, 2);
INSERT INTO `Comment` VALUES (null, "Wow great Story", 1, 3);
INSERT INTO `Comment` VALUES (null, "You write so well", 4, 4);
INSERT INTO `Comment` VALUES (null, "Amazing content", 3, 2);
INSERT INTO `Comment` VALUES (null, "I didn't like it so much", 2, 3);
INSERT INTO `Comment` VALUES (null, "Worst read ever!!", 2, 1);

DROP TABLE `Comment`;


CREATE TABLE `Posttag` (
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `postId` INTEGER NOT NULL,
    `tagId` INTEGER NOT NULL,
    FOREIGN KEY(`postId`) REFERENCES `Post`(`id`),
    FOREIGN KEY(`tagId`) REFERENCES `Tag`(`id`)
);

INSERT INTO `Posttag` VALUES (null, 3, 1);
INSERT INTO `Posttag` VALUES (null, 1, 1);
INSERT INTO `Posttag` VALUES (null, 3, 2);



INSERT INTO `Category` VALUES (null, "Programming");
INSERT INTO `Category` VALUES (null, "Nature");
INSERT INTO `Category` VALUES (null, "Food");



INSERT INTO `Posttag` VALUES (null, 2, 3);
INSERT INTO `Posttag` VALUES (null, 1, 1);
INSERT INTO `Posttag` VALUES (null, 4, 4);

DROP TABLE `Posttag`;

SELECT * FROM Tag;
SELECT * FROM Comment;
SELECT * FROM Category;
SELECT * FROM User;
SELECT * FROM Post;
SELECT * FROM Posttag;

