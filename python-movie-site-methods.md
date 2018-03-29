# Project 1 methods and review

**Udacity Full Stack Web Developer Nanodegree program**

Project 1. Python web server

Brendon Smith

br3ndonland

## TOC
<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [Code](#code)
- [Project Rubric](#project-rubric)
- [Initial submission](#initial-submission)
- [Re-submission](#re-submission)
- [Future directions](#future-directions)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->


## Code

* **I basically already completed the project by working through the [Programming foundations with Python](https://www.udacity.com/course/programming-foundations-with-python--ud036) course. The course was clearly helpful, and taught me what I needed to know!**
* I began by modifying the *fresh_tomatoes.py* code from the lessons.
* Renamed to *fresh_tomatoes_noir.py*
* Navbar: 
	- I modified the title of the page, and added the subtitle, *Shadows and Snappy Dialogue*, which is my one-line definition of film noir.
	- The *fresh_tomatoes.py* file provided by Udacity creates a header bar with a dead link over the title. There is no need to format the text as a link, because we are not including links and navigation. It is basically just a header bar. I reformatted the header text with `navbar-text`. 
* Movie tiles: Added movie year and storyline. Storylines are my original work.
* Reflow: changed reflow so that there are two movies per row, even in large browser windows. This keeps the movies together by era (classic/neo/future noir).


<!DOCTYPE html>
<html>
<body>
<div ui-view="" autoscroll="true" class="ng-scope" style=""><!-- uiView:  --><div ui-view="" autoscroll="true" class="ng-scope"><div ng-controller="RubricCtrl as ctrl" class="row ng-scope"> <div id="proj-spec-div" class="col-xs-offset-1 col-xs-10"> <h2 id="project-spec-headline" translate="" class="ng-scope">Project Rubric</h2> <h3 id="project-name" ng-bind-html="localize(ctrl.rubric.project, 'name', markup=true)" class="ng-binding"><p>Movie Trailer Website</p>
</h3>  <!-- ngRepeat: section in ctrl.rubric.sections --><div ng-repeat="section in ctrl.rubric.sections" class="ng-scope" style=""> <span class="rubric-section ng-binding" ng-bind-html="localize(section, 'name', markup=true)"><p><h3>Functionality</h3></p>
</span> <table class="table table-bordered section-table"> <thead> <tr> <!-- ngIf: !ctrl.hideCriteria --><th class="rubric-category criteria col-xs-3 ng-scope" ng-if="!ctrl.hideCriteria"> <span translate="" class="ng-scope">Criteria</span> </th><!-- end ngIf: !ctrl.hideCriteria --> <th class="rubric-category meets-specs" ng-class="ctrl.reviewerTips ? col-xs-7 : col-xs-4"> <span translate="" class="ng-scope">Meets Specifications</span> </th> <!-- ngIf: ctrl.reviewerTips --> </tr> </thead> <tbody>  <!-- ngRepeat: rubricItem in section.rubric_items --><tr ng-repeat="rubricItem in section.rubric_items" class="ng-scope"> <!-- ngIf: !ctrl.hideCriteria --><td class="rubric-item col-xs-3 ng-binding ng-scope" ng-if="!ctrl.hideCriteria" ng-bind-html="localize(rubricItem, 'criteria', markup=true)"><p>Is the page dynamically generated from a <code>Python</code> data structure?</p>
</td><!-- end ngIf: !ctrl.hideCriteria --> <td class="rubric-item ng-binding" ng-class="ctrl.reviewerTips ? col-xs-7 : col-xs-4" ng-bind-html="localize(rubricItem, 'passed_description', markup=true)"><p>Page is dynamically generated from a <code>Python</code> data structure.</p>
</td> <!-- ngIf: ctrl.reviewerTips --> </tr><!-- end ngRepeat: rubricItem in section.rubric_items --><tr ng-repeat="rubricItem in section.rubric_items" class="ng-scope"> <!-- ngIf: !ctrl.hideCriteria --><td class="rubric-item col-xs-3 ng-binding ng-scope" ng-if="!ctrl.hideCriteria" ng-bind-html="localize(rubricItem, 'criteria', markup=true)"><p>Does the page present the required content (title, art, and link)?</p>
</td><!-- end ngIf: !ctrl.hideCriteria --> <td class="rubric-item ng-binding" ng-class="ctrl.reviewerTips ? col-xs-7 : col-xs-4" ng-bind-html="localize(rubricItem, 'passed_description', markup=true)"><p>Page does present required content (movie title, box art and trailer link).</p>
</td> <!-- ngIf: ctrl.reviewerTips --> </tr><!-- end ngRepeat: rubricItem in section.rubric_items --><tr ng-repeat="rubricItem in section.rubric_items" class="ng-scope"> <!-- ngIf: !ctrl.hideCriteria --><td class="rubric-item col-xs-3 ng-binding ng-scope" ng-if="!ctrl.hideCriteria" ng-bind-html="localize(rubricItem, 'criteria', markup=true)"><p>Is the page error free?</p>
</td><!-- end ngIf: !ctrl.hideCriteria --> <td class="rubric-item ng-binding" ng-class="ctrl.reviewerTips ? col-xs-7 : col-xs-4" ng-bind-html="localize(rubricItem, 'passed_description', markup=true)"><p>Page is error free.</p>
</td> <!-- ngIf: ctrl.reviewerTips --> </tr><!-- end ngRepeat: rubricItem in section.rubric_items --> </tbody> </table> </div><!-- end ngRepeat: section in ctrl.rubric.sections --><div ng-repeat="section in ctrl.rubric.sections" class="ng-scope"> <span class="rubric-section ng-binding" ng-bind-html="localize(section, 'name', markup=true)"><p><h3>Code Quality</h3></p>
</span> <table class="table table-bordered section-table"> <thead> <tr> <!-- ngIf: !ctrl.hideCriteria --><th class="rubric-category criteria col-xs-3 ng-scope" ng-if="!ctrl.hideCriteria"> <span translate="" class="ng-scope">Criteria</span> </th><!-- end ngIf: !ctrl.hideCriteria --> <th class="rubric-category meets-specs" ng-class="ctrl.reviewerTips ? col-xs-7 : col-xs-4"> <span translate="" class="ng-scope">Meets Specifications</span> </th> <!-- ngIf: ctrl.reviewerTips --> </tr> </thead> <tbody>  <!-- ngRepeat: rubricItem in section.rubric_items --><tr ng-repeat="rubricItem in section.rubric_items" class="ng-scope"> <!-- ngIf: !ctrl.hideCriteria --><td class="rubric-item col-xs-3 ng-binding ng-scope" ng-if="!ctrl.hideCriteria" ng-bind-html="localize(rubricItem, 'criteria', markup=true)"><p>Is the code ready for personal review and neatly formatted according to the Python PEP-8 Guidelines?</p>
</td><!-- end ngIf: !ctrl.hideCriteria --> <td class="rubric-item ng-binding" ng-class="ctrl.reviewerTips ? col-xs-7 : col-xs-4" ng-bind-html="localize(rubricItem, 'passed_description', markup=true)"><p>Code is ready for personal review and neatly formatted. Students should follow the Python <a href="http://pep8online.com/" target="_blank">PEP-8 Guidelines</a></p>
</td> <!-- ngIf: ctrl.reviewerTips --> </tr><!-- end ngRepeat: rubricItem in section.rubric_items --> </tbody> </table> </div><!-- end ngRepeat: section in ctrl.rubric.sections --><div ng-repeat="section in ctrl.rubric.sections" class="ng-scope"> <span class="rubric-section ng-binding" ng-bind-html="localize(section, 'name', markup=true)"><p><h3>Comments</h3></p>
</span> <table class="table table-bordered section-table"> <thead> <tr> <!-- ngIf: !ctrl.hideCriteria --><th class="rubric-category criteria col-xs-3 ng-scope" ng-if="!ctrl.hideCriteria"> <span translate="" class="ng-scope">Criteria</span> </th><!-- end ngIf: !ctrl.hideCriteria --> <th class="rubric-category meets-specs" ng-class="ctrl.reviewerTips ? col-xs-7 : col-xs-4"> <span translate="" class="ng-scope">Meets Specifications</span> </th> <!-- ngIf: ctrl.reviewerTips --> </tr> </thead> <tbody>  <!-- ngRepeat: rubricItem in section.rubric_items --><tr ng-repeat="rubricItem in section.rubric_items" class="ng-scope"> <!-- ngIf: !ctrl.hideCriteria --><td class="rubric-item col-xs-3 ng-binding ng-scope" ng-if="!ctrl.hideCriteria" ng-bind-html="localize(rubricItem, 'criteria', markup=true)"><p>Are comments effectively used to explain longer code procedures?</p>
</td><!-- end ngIf: !ctrl.hideCriteria --> <td class="rubric-item ng-binding" ng-class="ctrl.reviewerTips ? col-xs-7 : col-xs-4" ng-bind-html="localize(rubricItem, 'passed_description', markup=true)"><p>Comments effectively explain longer code procedures.</p>
</td> <!-- ngIf: ctrl.reviewerTips --> </tr><!-- end ngRepeat: rubricItem in section.rubric_items --> </tbody> </table> </div><!-- end ngRepeat: section in ctrl.rubric.sections --><div ng-repeat="section in ctrl.rubric.sections" class="ng-scope"> <span class="rubric-section ng-binding" ng-bind-html="localize(section, 'name', markup=true)"><p><h3>Documentation</h3></p>
</span> <table class="table table-bordered section-table"> <thead> <tr> <!-- ngIf: !ctrl.hideCriteria --><th class="rubric-category criteria col-xs-3 ng-scope" ng-if="!ctrl.hideCriteria"> <span translate="" class="ng-scope">Criteria</span> </th><!-- end ngIf: !ctrl.hideCriteria --> <th class="rubric-category meets-specs" ng-class="ctrl.reviewerTips ? col-xs-7 : col-xs-4"> <span translate="" class="ng-scope">Meets Specifications</span> </th> <!-- ngIf: ctrl.reviewerTips --> </tr> </thead> <tbody>  <!-- ngRepeat: rubricItem in section.rubric_items --><tr ng-repeat="rubricItem in section.rubric_items" class="ng-scope"> <!-- ngIf: !ctrl.hideCriteria --><td class="rubric-item col-xs-3 ng-binding ng-scope" ng-if="!ctrl.hideCriteria" ng-bind-html="localize(rubricItem, 'criteria', markup=true)"><p>Is there a <code>README</code> file that include details of all steps required to successfully run the application?</p>
</td><!-- end ngIf: !ctrl.hideCriteria --> <td class="rubric-item ng-binding" ng-class="ctrl.reviewerTips ? col-xs-7 : col-xs-4" ng-bind-html="localize(rubricItem, 'passed_description', markup=true)"><p>A <code>README</code> file includes details of all the steps required to successfully run the application.</p>
</td> <!-- ngIf: ctrl.reviewerTips --> </tr><!-- end ngRepeat: rubricItem in section.rubric_items --> </tbody> </table> </div><!-- end ngRepeat: section in ctrl.rubric.sections --> <!-- ngIf: ctrl.rubric.stand_out --><div id="stand-out" ng-if="ctrl.rubric.stand_out" class="col-xs-offset-1 col-xs-10 ng-scope" style=""> <h3 id="stand-out-headline" class="text-center ng-scope" translate="">Suggestions to Make Your Project Stand Out!</h3> <div id="stand-out-text" ng-bind-html="localize(ctrl.rubric, 'stand_out', markup=true)" class="ng-binding"><ul>
<li>Alter the <code>HTML/CSS/JS</code> to improve the look of the page.</li>
<li>Use an <code>API</code> to supply movie data.</li>
</ul>
</div>
</div><!-- end ngIf: ctrl.rubric.stand_out -->
</div> 
</div>
</div>
</div>
</body>
</html>


## Initial submission

Reviewer comments:

> **Comments effectively explain longer code procedures.**
> 
> Commenting is always a good way to make your code more readable to other programmers. Starting to build good coding habits is key to becoming a great programmer.
> 
> Please see this link to read more about [Why is Documentation Extremely Important for Developers?](http://www.seguetech.com/why-is-documentation-extremely-important-for-developers/)
> 
> Here's a little example about how your comments should be like:
> <img src="https://udacity-reviews-uploads.s3.amazonaws.com/_attachments/3576/1504918475/8.png">


## Re-submission

Message to reviewer:

> Thank you very much for your constructive and helpful review of my movie website project. I have revised my code, and committed the changes to my GitHub repository.

Revisions:

* Added a docstring above the function definition in *media.py* to explain what the function does
* Added a standardized header in the first three lines of each file

**Revisions accepted!**

Reviewer comments:

> The code is very well documented and works fine :+1:
> Now you have a good knowledge of Functional Programming in Python. Keep on doing your good coding practices, and you'll become a great programmer :smiley::star:.!


## Future directions

* Use an API to supply movie data:
	- I was thinking about this while progressing through the course. It's silly to manually type in links and info for movies when you could just retrieve it.
	- I could use `requests` to call the data, and draw from an API like [The Movie DB](https://www.themoviedb.org/documentation/api) or [OMDB](https://www.omdbapi.com/). [Fandango/Rotten Tomatoes](https://developer.fandango.com/) requires an approval process.
* Update the webpage code for Bootstrap 4 and the CSS flexbox grid.
* Re-write the app with a Python framework like Flask.