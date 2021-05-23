var app = require('../server');
var AppController = require('../controllers/AppController');
var StudentsController = require('../controllers/StudentsController');

app.get('/', function (request, response) {
  AppController.getHomepage(request, response);
});

app.get('/students', function (request, response) {
  StudentsController.getAllStudents(request, response);
});

app.get('/students:major', function (request, response) {
  StudentsController.getAllStudentsByMajor(request, response);
});
