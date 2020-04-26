
class Card
{
    constructor(element)
    {
        this.buttons = element.getElementsByClassName("tab");
        this.tabs = element.getElementsByClassName("card-content");

        for(let i=0; i<this.buttons.length; i++)
        {
            this.buttons[i].onclick = function()
            { 
                this.disable_all_tabs()
                this.tabs[i].style.display = "block";
            }.bind(this)
        }
    }
    disable_all_tabs()
    {
        for(let b=0; b < this.tabs.length; b++)
        {
            this.tabs[b].style.display = "none";
        }
    }
}


window.addEventListener("load", function(){

    cards = document.getElementsByClassName("card");
    for(let i=0; i<cards.length; i++)
    {
        new Card(cards[i]);
    }    
});