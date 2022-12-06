



Day 1 - Advent of Code 2015





window.addEventListener('click', function(e,s,r){if(e.target.nodeName==='CODE'&&e.detail===3){s=window.getSelection();s.removeAllRanges();r=document.createRange();r.selectNodeContents(e.target);s.addRange(r);}});


# [Advent of Code](/)

* [[About]](/2015/about)
* [[Events]](/2015/events)
* [[Shop]](https://teespring.com/stores/advent-of-code)
* [[Log In]](/2015/auth/login)
#   {year=>[2015](/2015)}

* [[Calendar]](/2015)
* [[AoC++]](/2015/support)
* [[Sponsors]](/2015/sponsors)
* [[Leaderboard]](/2015/leaderboard)
* [[Stats]](/2015/stats)




## --- Day 1: Not Quite Lisp ---

Santa was hoping for a white Christmas, but his weather machine's "snow" function is powered by stars, and he's fresh out! To save Christmas, he needs you to collect *fifty stars* by December 25th.


Collect stars by helping Santa solve puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants *one star*. Good luck!


Here's an easy puzzle to warm you up.


Santa is trying to deliver presents in a large apartment building, but he can't find the right floor - the directions he got are a little confusing. He starts on the ground floor (floor `0`) and then follows the instructions one character at a time.


An opening parenthesis, `(`, means he should go up one floor, and a closing parenthesis, `)`, means he should go down one floor.


The apartment building is very tall, and the basement is very deep; he will never find the top or bottom floors.


For example:


* `(())` and `()()` both result in floor `0`.
* `(((` and `(()(()(` both result in floor `3`.
* `))(((((` also results in floor `3`.
* `())` and `))(` both result in floor `-1` (the first basement level).
* `)))` and `)())())` both result in floor `-3`.


To *what floor* do the instructions take Santa?



To play, please identify yourself via one of these services:


[[GitHub]](/auth/github) [[Google]](/auth/google) [[Twitter]](/auth/twitter) [[Reddit]](/auth/reddit) - [[How Does Auth Work?]](/about#faq_auth)





(function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
(i[r].q=i[r].q||[]).push(arguments)},i[r].l=1\*new Date();a=s.createElement(o),
m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
})(window,document,'script','//www.google-analytics.com/analytics.js','ga');
ga('create', 'UA-69522494-1', 'auto');
ga('set', 'anonymizeIp', true);
ga('send', 'pageview');



