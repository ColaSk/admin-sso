-- upgrade --
CREATE TABLE `role_permission` (`permission_id` INT NOT NULL REFERENCES `permission` (`id`) ON DELETE CASCADE,`roles_id` INT NOT NULL REFERENCES `roles` (`id`) ON DELETE CASCADE) CHARACTER SET utf8mb4;
CREATE TABLE `user_role` (`users_id` INT NOT NULL REFERENCES `users` (`id`) ON DELETE CASCADE,`role_id` INT NOT NULL REFERENCES `roles` (`id`) ON DELETE CASCADE) CHARACTER SET utf8mb4;
-- downgrade --
DROP TABLE IF EXISTS `role_permission`;
DROP TABLE IF EXISTS `user_role`;
