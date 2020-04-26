
class Card
{
    constructor(element)
    {
        this.buttons = element.getElementsByClassName("tab");
        this.tabs = element.getElementsByClassName("card-content");
        this.loaded = 0
        this.current_tab = 0
        this.show_more = document.getElementById("show_more");
        this.show_more.onclick = function()
        {
            this.show_50_more_recordings();
        }.bind(this);

        this.show_all = document.getElementById("show_all");
        this.show_all.onclick = function()
        {
            this.show_all_recordings();
        }.bind(this);


        for(let i=0; i<this.buttons.length; i++)
        {
            this.buttons[i].onclick = function()
            {
                this.loaded = 0;
                this.disable_all_tabs()
                this.tabs[i].style.display = "block";
                this.current_tab = i;
                this.show_50_more_recordings();
            }.bind(this)
        }
        this.tabs[0].style.display = "block";
        this.show_50_more_recordings();
    }
    disable_all_tabs()
    {
        // '-1' because the pagination doesn't count as a tab.
        for(let b=0; b < this.tabs.length-1; b++)
        {
            this.tabs[b].style.display = "none";
        }
    }

    disable_all_recordings()
    {
        let recordings = this.tabs[this.current_tab].getElementsByClassName("collapsible hoverable");
        for(let i=0; i<recordings.length; i++)
        {
            recordings[i].style.display = "none";
        }
    }

    show_50_more_recordings()
    {
        let recordings = this.tabs[this.current_tab].getElementsByClassName("collapsible hoverable");
        this.loaded +=1;
        if (this.loaded*50 >= recordings.length)
        {
            this.show_more.style.display = "none";
            this.show_all.style.display = "none";
        }
        else
        {
            this.show_more.style.display = "block";
            this.show_all.style.display = "block";
        }
        for(let i=0; i<recordings.length; i++)
        {
            if(i < this.loaded*50)
            {
                recordings[i].style.display = "block";
            }
            else
            {
                break;
            }
        }
    }
    show_all_recordings()
    {
        let recordings = this.tabs[this.current_tab].getElementsByClassName("collapsible hoverable");
        this.loaded += 100;
        this.show_more.style.display = "none";
        this.show_all.style.display = "none";

        for(let i=0; i<recordings.length; i++)
        {
            recordings[i].style.display = "block";
        }
    }
}

window.addEventListener("load", function()
{
    cards = document.getElementsByClassName("card");
    for(let i=0; i<cards.length; i++)
    {
        new Card(cards[i]);
    }
});