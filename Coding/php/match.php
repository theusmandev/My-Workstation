<?php


$day = 'Monday';

$Message = match($day){
    'Monday'=> 'Start of the week',
    "Friday" => 'End of the week',
    'Sunday' => 'Holiday',
    default => 'Just another day',
};
echo $Message;






?>
