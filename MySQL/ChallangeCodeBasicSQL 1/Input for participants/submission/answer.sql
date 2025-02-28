select *
from dim_customer1; 

select * 
from dim_customer1
where region = "apac";

select distinct customer
from dim_customer1;

select distinct region
from dim_customer1;

select distinct market
from dim_customer1;

-- req 1 
select market
from dim_customer1
where customer = 'atliq exclusive' and
region = 'apac'
group by market
order by market asc;

 -- req 2
 
 select *
 from fact_sales_monthly1;
 
 select  *
 from dim_product1;
 
 select count(distinct(dp.product_code)), fiscal_year 
 from fact_sales_monthly1 as fcs
 join dim_product1 as dp
 on dp.product_code = fcs.product_code
 where fiscal_year = 2021
 ;
 
 with unique_product_2020 as(
select count(distinct(dp.product)) as unique_product2020, fiscal_year 
 from fact_sales_monthly1 as fcs
 join dim_product1 as dp
 on dp.product_code = fcs.product_code 
 where fiscal_year = 2020
 ), unique_product_2021 as(
 select count(distinct(dp.product)) as unique_product2021, fiscal_year 
 from fact_sales_monthly1 as fcs
 join dim_product1 as dp
 on dp.product_code = fcs.product_code
 where fiscal_year = 2021
 )select unique_product_2020.unique_product2020, unique_product_2021.unique_product2021,
  ROUND((unique_product2021-unique_product2020)*100/unique_product2020, 2) AS percentage_chg
 from unique_product_2020, unique_product_2021;
 
 -- req 3
 
 select  *
 from dim_product1;
 
select  count(distinct(product)) as product_count, segment
from dim_product1
group by segment
order by 1 desc;

-- req 4
with unique_product_2020 as(
select count(distinct(dp.product)) as unique_product2020, fcs.fiscal_year, dp.segment 
 from fact_sales_monthly1 as fcs
 join dim_product1 as dp
 on dp.product_code = fcs.product_code 
 where fcs.fiscal_year = 2020
  group by fcs.fiscal_year ,dp.segment
 ), unique_product_2021 as(
 select count(distinct(dp.product)) as unique_product2021, fcs.fiscal_year, dp.segment 
 from fact_sales_monthly1 as fcs
 join dim_product1 as dp
 on dp.product_code = fcs.product_code
 where fcs.fiscal_year = 2021
 group by fcs.fiscal_year,dp.segment
 ), segment as (
select segment
from dim_product1
 )select unique_product_2020.unique_product2020 as unique_product2020,
unique_product_2021.unique_product2021 as unique_product2021,
 unique_product_2021.segment, (unique_product2021-unique_product2020) as difference
 from unique_product_2020, unique_product_2021
 where  unique_product_2021.segment = unique_product_2020.segment
 order by 3 asc;
 
 -- req 5
 select manufacturing_cost, dp.product, fmc.product_code
 from fact_manufacturing_cost1 as fmc
 join dim_product1 as dp
 on fmc.product_code = dp.product_code
 where manufacturing_cost in
 (
 select max(manufacturing_cost)
 from fact_manufacturing_cost1
 union
 select min(manufacturing_cost)
 from fact_manufacturing_cost1
 );
 
 -- req 6
 
 select *
 from fact_pre_invoice_deductions1;
 
  select *
 from dim_customer1;
 
 select  dc.customer_code, dc.customer, round(avg(fpid.pre_invoice_discount_pct),3) as average_discount_percentage
 from dim_customer1 as dc
 join fact_pre_invoice_deductions1 as fpid
 on dc.customer_code = fpid.customer_code
 where dc.market = 'india' and fpid.fiscal_year = 2021
 group by dc.customer, dc.customer_code 
 order by 3 desc
 limit 5
 ;
 
 -- req 7

select * 
from fact_gross_price1;

select *
from dim_customer1
where customer = 'atliq exclusive';

select *
from fact_sales_monthly;

select fsm.fiscal_year as years, CONCAT(MONTHNAME(fsm.date), ' (', YEAR(fsm.date), ')') AS months,
round(sum(fsm.sold_quantity * fgp.gross_price),2) as  gross_sales_amount
from dim_customer1 as dc
join fact_sales_monthly as fsm
on dc.customer_code = fsm.customer_code
join fact_gross_price1 as fgp
on fsm.product_code = fgp.product_code
where customer = 'atliq exclusive'
group by months, fsm.fiscal_year
order by years ;

-- req 8

select *
from fact_sales_monthly1;

select count(distinct(`date`))
from fact_sales_monthly1
where fiscal_year = 2020
order by `date` asc; 

select distinct(`date`)
from fact_sales_monthly1
where fiscal_year = 2020
order by `date` asc; 

select
case
	when `date` between '2019-09-01' and '2019-11-01' then 1
    when `date` between '2019-12-01' and '2020-02-01' then 2
    when `date` between '2020-03-01' and '2020-05-01' then 3
    when `date` between '2020-06-01' and '2020-08-01' then 4
end as quarters, sum(sold_quantity) as total_sold_quantity
from fact_sales_monthly1
where fiscal_year = 2020
group by quarters
order by total_sold_quantity DESC;


-- req 9
select *
from dim_customer1; 

select *
from fact_gross_price1;

select *
from fact_sales_monthly1; 

select distinct(dc.channel), fsm.fiscal_year, round(sum(fgp.gross_price * fsm.sold_quantity/1000000),2) as gross_sales_mln
from dim_customer1 as dc
join fact_sales_monthly as fsm
on dc.customer_code = fsm.customer_code
join fact_gross_price1 as fgp
on fgp.product_code = fsm.product_code
where fsm.fiscal_year = 2021
group by dc.channel
order by 3 desc
;

with output as(
select distinct(dc.channel) as uniqueChannel, fsm.fiscal_year, 
round(sum(fgp.gross_price * fsm.sold_quantity/1000000),2) as gross_sales_mln
from dim_customer1 as dc
join fact_sales_monthly as fsm
on dc.customer_code = fsm.customer_code
join fact_gross_price1 as fgp
on fgp.product_code = fsm.product_code
where fsm.fiscal_year = 2021
group by dc.channel
)select uniqueChannel, 
CONCAT(Gross_sales_mln,' M') AS Gross_sales_mln , CONCAT(ROUND(Gross_sales_mln*100/total , 2), ' %') AS percentage 
from(
(select sum(gross_sales_mln) as total 
from output) a, (SELECT * FROM output) b)
order by 3 desc
;

-- req 10

select *
from fact_sales_monthly1;

select * 
from dim_product;

select dp.division, dp.product_code, dp.product ,sum(fsm.sold_quantity) as total_sold_quantity
from dim_product1 as dp
join fact_sales_monthly1 as fsm
on dp.product_code = fsm.product_code
where fsm.fiscal_year = 2021
group by dp.division, dp.product_code, dp.product
order by 4 desc;

with cte1 as(
select dp.division, dp.product_code, dp.product ,sum(fsm.sold_quantity) as total_sold_quantity
from dim_product1 as dp
join fact_sales_monthly1 as fsm
on dp.product_code = fsm.product_code
where fsm.fiscal_year = 2021
group by dp.division, dp.product_code, dp.product
), cte2 AS 
(
SELECT division, product_code, product, total_sold_quantity,
RANK() OVER(PARTITION BY division ORDER BY total_sold_quantity DESC) AS 'Rank_Order' 
FROM cte1
)SELECT cte1.division, cte1.product_code, cte1.product, cte2.total_sold_quantity, cte2.Rank_Order
FROM cte1 JOIN cte2
 ON cte1.product_code = cte2.product_code
WHERE cte2.Rank_Order IN (1,2,3);

