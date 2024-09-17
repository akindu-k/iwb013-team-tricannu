import ballerina/io;

public function main(){
    io:println(helloworld("Hello Akindu"));
}

function helloworld(string name) returns string {
    return name;
}