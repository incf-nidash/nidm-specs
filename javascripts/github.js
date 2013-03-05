var github = (function(){
    function render(target, repos){
        var i = 0, t = $(target)[0];
        var fragment = '<li>INCF Github Repos</li>';

        for(i = 0; i < repos.length; i++) {
            fragment += '<li><a href="'+repos[i].html_url+'">'+repos[i].name+'</a></li>';
        }
        t.innerHTML = fragment;
    }
    return {
        showRepos: function(options){
            $.get("https://api.github.com/users/"+options.user+"/repos?sort=pushed"
                , function(data) {
                    var repos = [];
                    if (!data) { return; }
                    for (var i = 0; i < data.length; i++) {
                        if (options.skip_forks && data[i].fork) { continue; }
                        repos.push(data[i]);
                    }
                    if (options.count) { repos.splice(options.count); }
                    render(options.target, repos);
                }
            );
        }
    };
})();
