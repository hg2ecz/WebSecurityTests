<html>
<body>
<?php
if (isset($_GET["neve"])) {
    echo "Hello $_GET[neve]!<br/>";
}
?>

<p>--------------------------<br/>
Írj be egy nevet.</p>
<form name="teszt" action="">
    <input type="text" name="neve">
    <input type="submit" value="Mehet">
</form>
</body>
</html>
