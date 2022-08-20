-- upgrade --
ALTER TABLE `api_permission` ADD `menu_id` INT NOT NULL  COMMENT '菜单id';
CREATE TABLE IF NOT EXISTS `role_and_menu` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT COMMENT '主键',
    `role_id` INT NOT NULL  COMMENT '角色id',
    `menu_id` INT NOT NULL  COMMENT '菜单id',
    KEY `idx_role_and_me_role_id_9cac9b` (`role_id`),
    KEY `idx_role_and_me_menu_id_218017` (`menu_id`)
) CHARACTER SET utf8mb4 COMMENT='角色与菜单权限中间表';;
CREATE TABLE IF NOT EXISTS `user_and_role` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT COMMENT '主键',
    `user_id` INT NOT NULL  COMMENT '用户id',
    `role_id` INT NOT NULL  COMMENT '角色id',
    KEY `idx_user_and_ro_user_id_cf022c` (`user_id`),
    KEY `idx_user_and_ro_role_id_2dca3d` (`role_id`)
) CHARACTER SET utf8mb4 COMMENT='用户角色中间表';-- downgrade --
ALTER TABLE `api_permission` DROP COLUMN `menu_id`;
DROP TABLE IF EXISTS `role_and_menu`;
DROP TABLE IF EXISTS `user_and_role`;
