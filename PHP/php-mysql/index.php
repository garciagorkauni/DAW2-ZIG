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
    <table>
        <thead>
            <tr>
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
</body>
</html>
