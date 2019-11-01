<html>
<body>
<?php
if (isset($_GET["id"])) {
    $conn = new mysqli("localhost", "test", "testpass", "test");
    if ($conn->connect_error) { die("Connection failed: " . $conn->connect_error); }

    $sql = "SELECT id, firstname, lastname FROM testtable where id > 2 and id = \"$_GET[id]\"";

    $result = $conn->query($sql);
    if (mysqli_num_rows($result) == 0) echo "Nincs adat";
        while($row = $result->fetch_assoc()) {
        echo "id: " . $row["id"]. " - Name: " . $row["firstname"]. " " . $row["lastname"]. "<br>";
    }
}
?>
<p>--------------------------<br/>
3-as értékre ad eredményt.</p>
<form name="teszt" action="">
    <input type="text" name="id">
    <input type="submit" value="Mehet">
</form>
</body>
</html>
