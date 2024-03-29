# admin sso

- [x] 开发中
- [ ] 优化中
- [ ] 开发完成

## brief (简介)

- 在开发过程中一直比较忽视用户管理、权限管理、登录解决方案方面的功能，认为这方面过于简单，但是在工作过程中发现类似的功能作为整个系统的基础模块尤为重要，对于整个业务有这不可忽视的作用，所以搜索了很多资料后决定搞一个通用的登录，权限的解决方案，深入理解一下用户管理方面的基础方案

## functions (功能)

- [ ] sso 单点登录
- [ ] 用户管理
- [ ] 权限管理

## 部署

- 数据库部署

```shell
aerich init -t config.ORM_LINK_CONF
aerich init-db # 初始化
aerich migrate --name drop_column # 更新迁移
aerich upgrade # 升级迁移到数据库数据库 

```

- 启动

```shell
uvicorn apps.application:app
```

## libs (库)

fastapi

## catalogue (目录)
