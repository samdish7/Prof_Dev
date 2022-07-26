# Notes for COMP3017; Sam Disharoon

## HTML > HyperText Markup Language

HTML is the standard language for making webpages. This is what users see when they open up a web browser and surf the web

# Section 1; Page Setup

Each proper HTML document has each of __DOCTYPE__, html tag, head tag, and a body tag. 

You can also use _paragraph tags_ to wrap text, _line breaks_, and _anchor tags_. 

Many other types of tags such as:

* < pre >
* < p >
* < ol >
* < ul >
* < li >

You are able to add special characters with the _&_ symbol.

Good HTML has 4 elements:
- __DOCTYPE__: This says to draw the page _normally_. 
	* HTML5 -> <!DOCTYPE html>
- __html__: This wraps the entire page
- __head__: The contains the metadata of the page, some example tags are:
	* script
	* style
	* link
	* title
	* meta
at MINIMUM, head should contain the following:
<head>
	<meta charset="utf-8">
	<meta name="viewport" 
	 content="width=device-width, intial-scale=1">
	<title>This is a web page</title>
</head>

- __body__: Contains all the info displayed on the page. There are TONS of examples of these types of tags, some are:
	* img
	* input
	* label
	* div
	* table
	* id
	* class
Tags can also have _attributes_ which further describe the tag. 

Although there are __MANY__ tags for layouts, the two most common are:
- div: a division or area of a page
- span: allows us to group things without disrupting the flow of text before and after

_a_ is a very useful tag. It allows us to include links into our webpages. This is called the anchor tag. You can even send text messages and do plenty of other things as well with this tag.

Use the _img__ tag to include images. You can handle the __alt__ attribute by always including it for one, but also should always be text, and keep the title very short. Do not just call it 'image' or 'photo'.

Generally want to avoid the __title__ tag. 

# Debugging your HTML and CSS

Because they are _run_ in a browser, that means they must be _debugged_ in your browser. So there is a lot of trial and error.

You can access all browsers' debugger because they are baked right in for us to use! You just right click and press __Inspect__. This provides a ton of information for you to digest. This is helpful because you can change the __local__ copy of your webpage, thus you can make changes to it without breaking anything on the server. 

You can examine network traffic, the sources of all the items in HTML, as well as work with CSS and simulate mobile devices. 

# Effective CSS Styling

All styles flow from the entire site to all the pages, sections and elements. Unless overriden, the lowest one wins.

CSS is here to get rid of old, outdated, and bandwidth-eating html tags. 

Style elements are __additive__. The hierarchy is: 

1. Style
2. id
3. class
4. element

The higher up in the list, the higher the priority. You can specify something that can't be overriden by using __!important__. __DO NOT DO THIS!__ Can lead to many headaches trying to debug. 

Some values in CSS are quite... cumbersome, so the solution to this is to create variables that store the values so you can use them in a more simple fashion. 

# Semantic Grouping

HTML5 semantic elements communicate _meaning_. A __nav__ section is used with links or to parts within the page. 

A __header__ contains the stuff at the top of a section as well as a __footer__ contains the stuff at the bottom of the section.
