1、登录数据库后，使用use命令切换使用的数据库
2、使用 source命令依次执行dtlab_init_schema.sql和dtlab_init_data.sql文件
3、命令格式为：source [PATH]\*.sql 注意斜线方向
4、执行成功后可以使用show tables; select * from user;等命令检查是否插入成功