(function(angular){


	var bieApp = angular.module('bieApp',[]);
	bieApp.controller('MainController',['$scope', '$log','$http', function($scope, $log, $http){
		$scope.key = ''
		$scope.recordsFound = false
		$scope.searching = false

		$scope.survey = function(key) {

			$scope.recordsFound = false
			$scope.matchedRecords = []
			if(key && key.trim()){
				$log.info("search for", key)
				$scope.searching = true
				$http.get('/rest_service/survey?key=' + key).then(
					function successCallback(response){
						$log.info("response", response)
						$scope.matchedRecords = response.data
						$scope.recordsFound = true
						$scope.searching = false
					},
					function errorCallback(response) {
						$log.error("response", response)
						$scope.searching = false
					}
				)
			}
		}

	}])


})(window.angular);
