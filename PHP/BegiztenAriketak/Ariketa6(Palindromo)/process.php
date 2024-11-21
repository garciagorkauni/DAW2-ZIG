<!DOCTYPE html>
<html lang="eu">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Palindromoa</title>
    <style>
        body {
            font-family: Arial, sans-serif;
        }
        h1 {
            color: blue;
            text-align: center;
        }
        .container {
            width: 50%;
            margin: 20px auto;
            border: 1px solid #000;
            padding: 20px;
            text-align: center;
        }
        .form-group {
            margin-bottom: 15px;
        }
        select, input[type="number"], button {
            padding: 5px;
            font-size: 16px;
        }
        .footer {
            text-align: center;
            margin-top: 20px;
        }
        .footer p {
            font-size: 12px;
            color: gray;
        }
    </style>
</head>
<body>
    <h1>Palindromoa</h1>
    <div class="container">
        <?php 
        if ($_POST["number"] == '') {
            echo "Zenbaki bat sartu behar duzu";
        } else {
            if(palindromoa($_POST["number"])){
                echo $_POST["number"] . ' zenbakia palindromoa da.';
            } else {
                echo $_POST["number"] . ' zenbakia ez da palindromoa.';
            }
        }
        ?>
    
    </div>
    [<a href="./index.html" >ITZULI</a>]
</body>
<?php 
function palindromoa($number) {
    $alderantziz = '';
    $original = $number;
    
    do {
        $alderantziz .= (int)$number % 10;
        $number = (int)$number/10;
        if ($number <= 1) {
            break;
        }
    } while (true);

    if($original == $alderantziz){
        return true;
    } else {
        return false;
    }
}
?>
</html>
