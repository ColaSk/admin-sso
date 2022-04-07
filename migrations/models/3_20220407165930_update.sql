-- upgrade --
ALTER TABLE `users` ADD `is_admin` BOOL NOT NULL  COMMENT 'Background administrator, only for background module' DEFAULT 0;
-- downgrade --
ALTER TABLE `users` DROP COLUMN `is_admin`;
