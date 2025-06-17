<?php
class user{
    public $name;
    public $email;

    public function __construct($name,$email)
    {
        $this->name=$name;
        $this->email=$email;
        
    }
     public function displayInfo() {
        echo "Name: $this->name <br>";
        echo "Email: $this->email <br><br>";
    }

}

$user1 = new user('usman','usman@gmail.com');
$user2 = new user('ali','ali@gmail.com');


$user1->displayInfo();
$user2->displayInfo();

?>
