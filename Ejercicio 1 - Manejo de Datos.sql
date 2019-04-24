-- EJERCICIO A
DROP TABLE IF EXISTS  movimientos_full
CREATE TEMP TABLE movimientos_full AS (
	SELECT m.fecha AS "fecha",
		   c.cod_cliente AS "codigo_cliente"
		   c.descripcion AS "descripcion_cliente",
		   v.descripcion AS "descripcion_proveedor",
		   p.descripcion AS "descripcion_producto",
		   t.descripcion AS "descripcion_marca",
		   m.cantidad AS "cantidad",
		   m.costo AS "costo",
		   m.venta AS "venta",
		   (m.venta - m.costo) AS "ganancia_neta"
	FROM etermax.data_movimientos m
	INNER JOIN etermax.data_clientes c ON c.cod_cliente = m.cod_cliente
	INNER JOIN etermax.data_productos p ON p.cod_prod = m.cod_prod
	INNER JOIN etermax.data_proovedores v ON v.cod_proveedor = p.cod_proveedor
	INNER JOIN etermax.data_marcas t ON t.cod_marca = p.cod_marca
);


-- EJERCICIO B
SELECT b.descripcion AS "Marca"
FROM etermax.data_marcas b
INNER JOIN etermax.data_productos p ON b.cod_marca = p.cod_marca
LEFT JOIN etermax.data_movimientos m ON p.cod_prod = m.cod_prod
WHERE m.fecha IS NULL;

-- EJERCICIO C
WITH tmp_movimientos_full AS (
	select 	x.fecha,
			x.descripcion_cliente,
			x.descripcion_proveedor,
			x.descripcion_producto,
			x.descripcion_producto,
			x.cantidad,
			x.costo,
			x.venta,
			(x.venta - x.costo) as rentabilidad_venta,
			row_number() over (partition by x.descripcion order by x.fecha desc) as cliente_operaciones
	from movimientos_full x
	where x.fecha = 'fecha_consulta' and x.codigo_cliente= 'cliente_consulta'
) 
SELECT fecha AS "Fecha", descripcion_cliente AS "Descripción de Cliente", SUM(rentabilidad_venta) AS "Ganancia Neta Acumulada"
FROM tmp_movimientos_full
WHERE cliente_operaciones < 8
GROUP BY 1, 2
ORDER BY 1, 2;