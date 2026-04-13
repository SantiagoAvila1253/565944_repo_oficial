# ============================================================
# OPERACIONES CRUD BÁSICAS (con diccionarios)
# ============================================================

# CRUD = Create, Read, Update, Delete
# Son las 4 operaciones fundamentales sobre cualquier conjunto de datos.

productos = [
    {
        "id_producto": 1,
        "categoria": "Escritura",
        "nombre": "Lápiz negro HB",
        "precio_unitario": 350,
    },
    {
        "id_producto": 2,
        "categoria": "Escritura",
        "nombre": "Bolígrafo azul",
        "precio_unitario": 500,
    },
]


# --- CREATE: agregar un nuevo registro ---
producto_3 = {
    "id_producto": 3,
    "categoria": "Escritura",
    "nombre": "Marcador permanente",
    "precio_unitario": 1200,
}
productos.append(producto_3)
print("\n[CREATE] Producto agregado:", producto_3)


# --- READ: buscar un registro por su clave primaria ---
id_buscado = 2
resultado = None
for p in productos:
    if p["id_producto"] == id_buscado:
        resultado = p
        break  # encontramos el registro, no hace falta seguir buscando
print(f"\n[READ] Producto con id {id_buscado}:", resultado)


# --- UPDATE: modificar un atributo de un registro existente ---
for p in productos:
    if p["id_producto"] == 1:
        p["precio_unitario"] = 400  # actualizamos el precio
        print("\n[UPDATE] Precio actualizado:", p)
        break


# --- DELETE: eliminar un registro por su clave primaria ---
id_a_eliminar = 3

for p in productos:
    if p["id_producto"] == id_a_eliminar:
        productos.remove(p)
        break  # importante para evitar problemas al modificar la lista

print(f"\n[DELETE] Tabla luego de eliminar id {id_a_eliminar}:")
for p in productos:
    print(p)
