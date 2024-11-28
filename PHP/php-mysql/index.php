<!DOCTYPE html>
<html lang="eu">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Etxebizitzen Taula</title>
    <style>
        table {
            width: 100%;
            border-collapse: collapse;
        }
        th, td {
            border: 1px solid #ddd;
            padding: 8px;
            text-align: left;
        }
        th {
            background-color: #f4f4f4;
        }
        img {
            max-width: 100px;
            height: auto;
        }
    </style>
</head>
<body>
    <h1>Etxebizitzen Zerrenda</h1>
    <form action="delete_records.php" method="POST">
        <table>
            <thead>
                <tr>
                    <th>Ezabatu</th>
                    <th>Mota</th>
                    <th>Zonaldea</th>
                    <th>Helbidea</th>
                    <th>Logelak</th>
                    <th>Prezioa</th>
                    <th>Tamaina</th>
                    <th>Extrak</th>
                    <th>Irudia</th>
                </tr>
            </thead>
            <tbody>
                <?php include 'process.php'; ?>
            </tbody>
        </table>
        <br>
        <button type="submit">Etxebizitzak ezabatu</button>
    </form>
    <br>
    <a href="form.php"><button>Etxebizitza berria gehitu</button></a>
</body>
</html>
