-- upgrade --
ALTER TABLE `api_permission` MODIFY COLUMN `extra_info` JSON   COMMENT '扩展信息';
ALTER TABLE `menu_permission` MODIFY COLUMN `parent_node_id` VARCHAR(255)   COMMENT '树的父节点id';
ALTER TABLE `menu_permission` MODIFY COLUMN `extra_info` JSON   COMMENT '扩展信息';
ALTER TABLE `roles` MODIFY COLUMN `extra_info` JSON   COMMENT '扩展信息';
ALTER TABLE `users` MODIFY COLUMN `extra_info` JSON   COMMENT '扩展信息';
-- downgrade --
ALTER TABLE `roles` MODIFY COLUMN `extra_info` JSON NOT NULL  COMMENT '扩展信息';
ALTER TABLE `users` MODIFY COLUMN `extra_info` JSON NOT NULL  COMMENT '扩展信息';
ALTER TABLE `api_permission` MODIFY COLUMN `extra_info` JSON NOT NULL  COMMENT '扩展信息';
ALTER TABLE `menu_permission` MODIFY COLUMN `parent_node_id` VARCHAR(255) NOT NULL  COMMENT '树的父节点id';
ALTER TABLE `menu_permission` MODIFY COLUMN `extra_info` JSON NOT NULL  COMMENT '扩展信息';
