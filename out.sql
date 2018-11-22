BEGIN;
CREATE TABLE `vector_virus` (
    `virus_id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `virus_name` varchar(100) NOT NULL
)
;
CREATE TABLE `vector_lab` (
    `lab_id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `lab_name` varchar(100) NOT NULL
)
;
CREATE TABLE `vector_person` (
    `person_id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `person_first` varchar(30) NOT NULL,
    `person_last` varchar(30) NOT NULL,
    `person_pass` varchar(30) NOT NULL,
    `person_email` varchar(30) NOT NULL,
    `lab_id` integer NOT NULL,
    `user_id` integer NOT NULL UNIQUE,
    UNIQUE (`person_first`, `person_last`)
)
;
ALTER TABLE `vector_person` ADD CONSTRAINT `lab_id_refs_lab_id_abdb1a28` FOREIGN KEY (`lab_id`) REFERENCES `vector_lab` (`lab_id`);
ALTER TABLE `vector_person` ADD CONSTRAINT `user_id_refs_id_cfbd6f62` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
CREATE TABLE `vector_recipientout` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `checkout_id` integer NOT NULL,
    `recipient_id` integer NOT NULL,
    `recipientout_created` datetime NOT NULL
)
;
CREATE TABLE `vector_checkout` (
    `checkout_id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `person_requested_id` integer NOT NULL,
    `person_checkedout_id` integer,
    `checkout_quantity` numeric(20, 4) NOT NULL,
    `virus_id` integer NOT NULL,
    `checkout_request_date` datetime NOT NULL,
    `checkout_checkout_date` datetime,
    `checkout_created` datetime NOT NULL,
    `checkout_updated` datetime NOT NULL,
    `checkout_satisfied` bool NOT NULL
)
;
ALTER TABLE `vector_checkout` ADD CONSTRAINT `person_requested_id_refs_person_id_40ef5f7e` FOREIGN KEY (`person_requested_id`) REFERENCES `vector_person` (`person_id`);
ALTER TABLE `vector_checkout` ADD CONSTRAINT `person_checkedout_id_refs_person_id_40ef5f7e` FOREIGN KEY (`person_checkedout_id`) REFERENCES `vector_person` (`person_id`);
ALTER TABLE `vector_checkout` ADD CONSTRAINT `virus_id_refs_virus_id_4ca46c45` FOREIGN KEY (`virus_id`) REFERENCES `vector_virus` (`virus_id`);
ALTER TABLE `vector_recipientout` ADD CONSTRAINT `checkout_id_refs_checkout_id_b7490c06` FOREIGN KEY (`checkout_id`) REFERENCES `vector_checkout` (`checkout_id`);
CREATE TABLE `vector_recipient` (
    `recipient_id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `recipient_code` varchar(10),
    `recipient_label` varchar(50),
    `recipient_quantity` numeric(20, 4) NOT NULL,
    `recipient_quantfromrecipient` numeric(20, 4),
    `parent_recipient_id` integer,
    `checkin_id` integer NOT NULL,
    `recipient_create` datetime NOT NULL,
    `recipient_update` datetime NOT NULL,
    `recipient_out` bool NOT NULL,
    `recipient_initialquantity` numeric(20, 4) NOT NULL
)
;
ALTER TABLE `vector_recipientout` ADD CONSTRAINT `recipient_id_refs_recipient_id_36d9347c` FOREIGN KEY (`recipient_id`) REFERENCES `vector_recipient` (`recipient_id`);
ALTER TABLE `vector_recipient` ADD CONSTRAINT `parent_recipient_id_refs_recipient_id_921b9db` FOREIGN KEY (`parent_recipient_id`) REFERENCES `vector_recipient` (`recipient_id`);
CREATE TABLE `vector_supplier` (
    `supplier_id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `supplier_name` varchar(50) NOT NULL,
    `supplier_contact` varchar(30),
    `supplier_email` varchar(75),
    `supplier_address` longtext,
    `supplier_notes` longtext
)
;
CREATE TABLE `vector_plasmid` (
    `plasmid_id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `plasmid_name` varchar(50) NOT NULL,
    `supplier_id` integer NOT NULL,
    `plasmid_number` varchar(50),
    `plasmid_presentation` varchar(50),
    `plasmid_nameRegistry` varchar(50),
    `plasmid_tupesmark` varchar(50),
    `plasmid_manipulation` varchar(50),
    `plasmid_stor_at` varchar(50),
    `plasmid_notes` longtext
)
;
ALTER TABLE `vector_plasmid` ADD CONSTRAINT `supplier_id_refs_supplier_id_3cd3c2be` FOREIGN KEY (`supplier_id`) REFERENCES `vector_supplier` (`supplier_id`);
CREATE TABLE `vector_checkin` (
    `checkin_id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `owner_id` integer NOT NULL,
    `supplier_id` integer NOT NULL,
    `plasmid_id` integer,
    `virus_id` integer NOT NULL,
    `checkin_mta` longtext,
    `checkin_notes` longtext
)
;
ALTER TABLE `vector_checkin` ADD CONSTRAINT `plasmid_id_refs_plasmid_id_84eb638c` FOREIGN KEY (`plasmid_id`) REFERENCES `vector_plasmid` (`plasmid_id`);
ALTER TABLE `vector_checkin` ADD CONSTRAINT `supplier_id_refs_supplier_id_63d9d3d1` FOREIGN KEY (`supplier_id`) REFERENCES `vector_supplier` (`supplier_id`);
ALTER TABLE `vector_checkin` ADD CONSTRAINT `owner_id_refs_person_id_c35adba` FOREIGN KEY (`owner_id`) REFERENCES `vector_person` (`person_id`);
ALTER TABLE `vector_checkin` ADD CONSTRAINT `virus_id_refs_virus_id_53cd00bd` FOREIGN KEY (`virus_id`) REFERENCES `vector_virus` (`virus_id`);
ALTER TABLE `vector_recipient` ADD CONSTRAINT `checkin_id_refs_checkin_id_22aea321` FOREIGN KEY (`checkin_id`) REFERENCES `vector_checkin` (`checkin_id`);
CREATE TABLE `vector_project_members` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `project_id` integer NOT NULL,
    `person_id` integer NOT NULL,
    UNIQUE (`project_id`, `person_id`)
)
;
ALTER TABLE `vector_project_members` ADD CONSTRAINT `person_id_refs_person_id_2af234ac` FOREIGN KEY (`person_id`) REFERENCES `vector_person` (`person_id`);
CREATE TABLE `vector_project_checkout` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `project_id` integer NOT NULL,
    `checkout_id` integer NOT NULL,
    UNIQUE (`project_id`, `checkout_id`)
)
;
ALTER TABLE `vector_project_checkout` ADD CONSTRAINT `checkout_id_refs_checkout_id_36c46355` FOREIGN KEY (`checkout_id`) REFERENCES `vector_checkout` (`checkout_id`);
CREATE TABLE `vector_project` (
    `project_id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `project_name` varchar(50) NOT NULL,
    `project_desc` longtext,
    `project_create` datetime NOT NULL,
    `project_update` datetime NOT NULL
)
;
ALTER TABLE `vector_project_members` ADD CONSTRAINT `project_id_refs_project_id_d43125c9` FOREIGN KEY (`project_id`) REFERENCES `vector_project` (`project_id`);
ALTER TABLE `vector_project_checkout` ADD CONSTRAINT `project_id_refs_project_id_3df557a5` FOREIGN KEY (`project_id`) REFERENCES `vector_project` (`project_id`);
CREATE TABLE `vector_projectfile` (
    `projectfile_id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `projectfile_name` varchar(50) NOT NULL,
    `projectfile_file` varchar(150) NOT NULL,
    `project_id` integer NOT NULL
)
;
ALTER TABLE `vector_projectfile` ADD CONSTRAINT `project_id_refs_project_id_26ee97ed` FOREIGN KEY (`project_id`) REFERENCES `vector_project` (`project_id`);
COMMIT;
