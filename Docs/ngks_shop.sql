create database ngks_shop; #crie a base para rodar o migration no django

use ngks_shop;

#inserir os grupos na base
insert into sgu_grupos (nome, link) values ('SGU','/sgu');
insert into sgu_grupos (nome, link) values ('ESTOQUE','/estoque');
insert into sgu_grupos (nome, link) values ('FLUXO','/fluxo');
insert into sgu_grupos (nome, link) values ('PEDIDOS','/pedidos');
insert into sgu_grupos (nome, link) values ('CATALOGO','/catalogo');

#inserir as permissões para o usuário criado pelo comando "createsuperuser"
insert into sgu_permissions (groups, usuario_id) values ('SGU', 1);
insert into sgu_permissions (groups, usuario_id) values ('ESTOQUE', 1);
insert into sgu_permissions (groups, usuario_id) values ('FLUXO', 1);
insert into sgu_permissions (groups, usuario_id) values ('PEDIDOS', 1);
insert into sgu_permissions (groups, usuario_id) values ('CATALOGO', 1);

#insere permissão na tela de administraçãoptimize
update sgu_usuario set tipo = 'E' where id = 1;
