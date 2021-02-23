# TODO

- мы можем не только заказывать, но и отправлять товар - нужна таблица на отправки + на логи по конкретным отправкам

# Вариант 13

# Предметная облась

## Информационная система магазина автозапчастей

# Задача

```
⚠️ В таких блокак как этот находятся мои заметки
```

Магазин розничной торговли осуществляет заказ запчастей в различных странах.

```
Магазин всего один, у него есть список запчастей и список поставщиков
```

Ведется статистика продаж, отражающая спрос на те или иные детали, и, соответственно, потребность магазина в них (сколько единиц, на какую сумму, какого товара продано за последнее время) и на ее основе составляются заказы на требуемые товары.

```
Добавляем лог продаж и данные по наличию
```

Выбор поставщика на каждый конкретный заказ осуществляют менеджеры магазина. В заказах перечисляется наименование товара, количество. Если указанное наименование товара ранее не поставлялось, оно пополняет справочник номенклатуры товаров.

```
Помимо списка уже заказанных запчастей имеем справочник со всеми SKU + поставщиком на этот SKU
```

Поставщики бывают различных категорий: фирмы, непосредственно производящие детали, дилеры, небольшие производства, мелкие поставщики и магазины. В результате поставщики различных категорий имеют различающийся набор атрибутов.

```
У поставщика появляется `type`
```

Фирмы и дилеры - это самые надежные партнеры, они могут предложить полный пакет документов, скидки, а главное - гарантию, чего не может сделать небольшое производство или мелкий магазин. У них же (фирмы и дилеры) закупается большой объем продукции. Небольшое производство - это низкие цены, но никакой гарантии качества. В мелких лавках можно выгодно купить небольшое количество простых деталей, на которых сразу виден брак. Фирмы и дилеры поставляют детали на основе договоров, чего не делается для небольшого производства и мелкого магазина. В ходе маркетинговых работ изучается рынок поставщиков, в результате чего могут появляться новые поставщики и исчезать старые.

Когда ожидаются новые поставки, магазин собирает заявки от покупателей на свои товары. Груз приходит, производится его таможенное оформление, оплата пошлин, после чего он доставляется на склад в магазин. В первую очередь удовлетворяются заявки покупателей, а оставшийся товар продается в розницу.

```
Добавляем информацию о поставках (лог с транзитными пунктами, датами, статусами и т.д.)
```

В любой момент можно получить любую информацию о деталях, находящихся на складе, либо о поставляемых деталях. Детали хранятся на складе в определенных ячейках. Все ячейки пронумерованы. Касса занимается приемом денег от покупателей за товар, а так же производит возврат денег за брак. Брак, если это возможно, возвращается поставщику, который производит замену бракованной детали. Информация о браке (поставщик, фирма-производитель, деталь) фиксируется.

```
Добавляем информацию о браке
```

# Total

```
При работе с валютами flaot идут в далёкое плаванье, храним все цены в микро (умножаем обычную цену на 10^6 и кастим к uint)
```

## Таблицы

<details>

<summary> Product </summary>

| column           | type     | Primary Key | Unique | Allow Null | Default  | Refers to           | Description                           |
| ---------------- | -------- | ----------- | ------ | ---------- | -------- | ------------------- | ------------------------------------- |
| id               | uuid     | true        | true   | false      | new uuid |                     |                                       |
| SKU              | string   | false       | false  | false      |          |                     | SKU + seller_id combination is unique |
| amount_available | uinteger | false       | false  | false      | 0        |                     |                                       |
| sold             | uinteger | false       | false  | false      | 0        |                     |                                       |
| total_got        | uinteger | false       | false  | false      | 0        |                     |                                       |
| seller_id        | uuid     | false       | false  | false      |          |                     |                                       |
| seller           | Seller   | false       | false  | true       |          | Seller lk seller_id |                                       |
| price            | uinteger | false       | false  | false      |          |                     |                                       |
| tax_percentage   | uinteger | false       | false  | false      |          |                     |                                       |

</details>

<details>

<summary> Seller </summary>

| column     | type       | Primary Key | Unique | Allow Null | Default  | Refers to         | Description                                                                |
| ---------- | ---------- | ----------- | ------ | ---------- | -------- | ----------------- | -------------------------------------------------------------------------- |
| id         | uuid       | true        | true   | false      | new uuid |                   |                                                                            |
| type       | char       | false       | false  | false      |          |                   | 0=manufacturer / 1=dealer / 2=small manufacturer / 3=small dealer / 4=shop |
| name       | string     | false       | false  | false      |          |                   |                                                                            |
| products   | Product[]  | false       | false  | false      |          | Product.seller_id |                                                                            |
| deliveries | Delivery[] | false       | false  | false      |          | Deliver.seller_id |                                                                            |

</details>

<details>

<summary> Defectives </summary>

| column     | type     | Primary Key | Unique | Allow Null | Default  | Refers to             |
| ---------- | -------- | ----------- | ------ | ---------- | -------- | --------------------- |
| id         | uuid     | true        | true   | false      | new uuid |                       |
| product_id | uuid     | false       | true   | false      |          |                       |
| product    | Product  | false       | false  | false      |          | Product lk product_id |
| amount     | uinteger | false       | false  | false      | 0        |                       |

</details>

<details>

<summary> SellOperation </summary>

| column            | type              | Primary Key | Unique | Allow Null | Default  | Refers to |
| ----------------- | ----------------- | ----------- | ------ | ---------- | -------- | --------- |
| id                | uuid              | true        | true   | false      | new uuid |           |
| product_snapshots | Product[] (jsonb) | false       | false  | false      | [ ]      |           |
| subtotal          | uinteger          | false       | false  | false      | 0        |           |
| taxified_price    | uinteger          | false       | false  | false      | 0        |           |
| tax_percentage    | uinteger          | false       | false  | false      | 0        |           |
| tax               | uinteger          | false       | false  | false      | 0        |           |

</details>

<details>

<summary> Delivery </summary>

| column         | type                     | Primary Key | Unique | Allow Null | Default                       | Refers to                         | Description                          |
| -------------- | ------------------------ | ----------- | ------ | ---------- | ----------------------------- | --------------------------------- | ------------------------------------ |
| id             | uuid                     | true        | true   | false      | new uuid                      |                                   |                                      |
| operation_id   | uuid                     | false       | false  | false      |                               |                                   |                                      |
| operation      | uuid                     | false       | false  | false      | SellOperation lk operation_id |                                   |                                      |
| price          | uinteger                 | false       | false  | false      | 0                             |                                   |                                      |
| taxified_price | uinteger                 | false       | false  | false      | 0                             |                                   |                                      |
| tax_percentage | uinteger                 | false       | false  | false      | 0                             |                                   |                                      |
| tax            | uinteger                 | false       | false  | false      | 0                             |                                   |                                      |
| log            | ObtainingInfoLogRecord[] | false       | false  | false      |                               | DeliveryLogRecord fk operation_id |                                      |
| status         | char                     | false       | false  | false      | 0                             |                                   | none / rejected / in progress / done |

</details>

<details>

<summary> DeliveryLogRecord </summary>

| column           | type     | Primary Key | Unique | Allow Null | Default                 | Refers to |
| ---------------- | -------- | ----------- | ------ | ---------- | ----------------------- | --------- |
| id               | uuid     | true        | true   | false      | new uuid                |           |
| delivery_id      | uuid     | false       | false  | false      |                         |           |
| delivery         | uuid     | false       | false  | false      | Delivery lk delivery_id |           |
| location         | string   | false       | false  | false      | 'Unknown'               |           |
| datetime_arrived | DateTime | false       | false  | false      | new Date()              |           |
| datetime_left    | DateTime | false       | false  | true       | null                    |           |

</details>
