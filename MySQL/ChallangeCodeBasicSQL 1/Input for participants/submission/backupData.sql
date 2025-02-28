select *
from dim_customer;

select *
from dim_product;

select *
from fact_gross_price;

select * 
from fact_manufacturing_cost;

select *
from fact_pre_invoice_deductions;

select * 
from fact_sales_monthly;

-- --------------------------------------
-- creating backup table

create table dim_customer1
like dim_customer;

insert into dim_customer1
select *
from dim_customer;

select *
from dim_customer1;

create table dim_product1
like dim_product;

insert into dim_product1
select * 
from dim_product;

select *
from dim_product1;

create table fact_gross_price1
like fact_gross_price;

insert into fact_gross_price1
select *
from fact_gross_price;

select *
from fact_gross_price1;

create table fact_manufacturing_cost1
like fact_manufacturing_cost;

insert into fact_manufacturing_cost1
select * 
from fact_manufacturing_cost;

select *
from fact_manufacturing_cost1;

create table fact_pre_invoice_deductions1
like fact_pre_invoice_deductionsl;

insert into fact_pre_invoice_deductions1
select *
from fact_pre_invoice_deductions;

select * from fact_pre_invoice_deductions1;

create table fact_sales_monthly1
like fact_sales_monthly;

insert into fact_sales_monthly1
select *
from fact_sales_monthly;

select * 
from fact_sales_monthly1;


  