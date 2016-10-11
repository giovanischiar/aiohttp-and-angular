var app = angular.module('meuapp', []);
app.controller('meuapp', function($scope, $http) {
    $scope.getRoute = function() {
        $http({
            url: 'http://127.0.0.1:8080/route',
            method: 'GET',
        }).
        success(function(data) {
            $scope.isThereMessageFromServer = true;
            $scope.datafromserver = data;
        }).
        error(function(data) {
            alert("error: " + data);
        });
    }
})