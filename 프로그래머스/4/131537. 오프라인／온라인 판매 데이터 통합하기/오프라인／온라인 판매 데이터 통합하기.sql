-- 코드를 입력하세요
select * from (
    select date_format(sales_date, '%Y-%m-%d') as sales_date,
    product_id,
    user_id,
    sales_amount
    from online_sale
    union all
    select date_format(sales_date, '%Y-%m-%d') as sales_date,
    product_id,
    NULL,
    sales_amount
    from offline_sale
) as combined_sale
where year(combined_sale.sales_date) = 2022 and month(combined_sale.sales_date)=3
order by combined_sale.sales_date asc, combined_sale.product_id asc, combined_sale.user_id asc