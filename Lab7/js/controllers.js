var portfolioApp = angular.module('portfolioApp',[]);

portfolioApp.controller('GalleryListCtrl', function($scope)
{
    $scope.galleries = 
    [
        { 'title':'equalizer',
        'when':'Listopad 2016',
        'thumbnailUrl':'img/10.jpg'
        },
        { 'title':'kompresor',
        'when':'Grudzień 2016',
        'thumbnailUrl':'img/12.jpg'
        },
        { 'title':'reverb',
        'when':'Styczeń 2017',
        'thumbnailUrl':'img/11.jpg'
        },
        { 'title':'delay',
        'when':'Luty 2017',
        'thumbnailUrl':'img/13.jpg'
        },
        { 'title':'flanger',
        'when':'Kwiecień 2017',
        'thumbnailUrl':'img/14.jpg'
        },
        { 'title':'autotune pro',
        'when':'Grudzień 2017',
        'thumbnailUrl':'img/15.jpg'
        }
    ];
    $scope.sortList = 
    [
        {
            'label':'Alfabetycznie',
            'value':'title'
        },
        {
            'label':'Chronologicznie',
            'value':'when'
        },
        {
            'label':'Od Najnowszych',
            'value':'-when'
        },
    ];
    
});