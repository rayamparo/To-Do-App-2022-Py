create table user_info(
	user_info_id bigserial not null,
	user_info_email varchar (50) unique not null,
	user_info_password varchar (50) not null,
	usre_info_name varchar (40) not null,
	primary key (user_info_id)
);

create table to_do_note(
	owner_id bigserial references user_info(user_info_id) not null,
	to_do_id bigserial not null,
	to_do_note varchar(100),
	to_do_end_date date not null,
	to_do_completed boolean not null,
	to_do_priority boolean not null,
	primary key (to_do_id)
);