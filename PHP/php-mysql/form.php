<!DOCTYPE html>
<html lang="eu">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gehitu Etxebizitza</title>
</head>
<body>
    <h1>Etxebizitza Berria Gehitu</h1>
    <form action="add_record.php" method="POST" enctype="multipart/form-data">
        <label for="mota">Mota:</label>
        <select name="mota" id="mota" required>
            <option value="Pisua">Pisua</option>
            <option value="Txaleta">Txaleta</option>
            <option value="Etxea">Etxea</option>
        </select><br>

        <label for="zonaldea">Zonaldea:</label>
        <select name="zonaldea" id="zonaldea" required>
            <option value="Alde zaharra">Alde zaharra</option>
            <option value="Deustu">Deustu</option>
            <option value="Atxuri">Atxuri</option>
            <option value="Miribilla">Miribilla</option>
            <option value="Basurtu">Basurtu</option>
        </select><br>

        <label for="helbidea">Helbidea:</label>
        <input type="text" id="helbidea" name="helbidea" required><br>

        <label for="logelak">Logelak:</label>
        <select name="logelak" id="logelak" required>
            <option value="1">1</option>
            <option value="2">2</option>
            <option value="3">3</option>
            <option value="4">4</option>
            <option value="5">5</option>
        </select><br>

        <label for="prezioa">Prezioa (€):</label>
        <input type="number" step="0.01" id="prezioa" name="prezioa" required><br>

        <label for="tamaina">Tamaina (m²):</label>
        <input type="number" step="0.01" id="tamaina" name="tamaina" required><br>

        <label for="extrak">Extrak:</label>
        <input type="checkbox" name="extrak[]" value="Igerilekua"> Igerilekua
        <input type="checkbox" name="extrak[]" value="Lorategia"> Lorategia
        <input type="checkbox" name="extrak[]" value="Garajea"> Garajea<br>

        <label for="irudia">Irudia:</label>
        <input type="file" id="irudia" name="irudia" accept="image/*"><br>

        <button type="submit">Gorde</button>
    </form>
    <a href="index.php">Bueltatu</a>
</body>
</html>
