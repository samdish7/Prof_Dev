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

The __main__ tag is one of the newer tags introduced. ONLY 1 PER DOCUMENT! Also cannot be a descendent of an _article, footer, header, or nav_ element.

__details & summary__ tags allow collapsible regions without _JavaScript_. __figure__ allows for a more condense version of the same thing you can make with a div. 

The __aside__ element is a tag that describes content that is not considered "primary" to the webpage. Such examples could be: _author's note, related content, ads_. 

# How to Position with CSS

Positioning is key to a good webpage. Good positioning makes navigation easier, looks nicer, and is generally easier to maintain. 

__display__ lays out _me_ or the things _inside me_. Things that affect _me_:
* block
* inline
* inline-block

Things that affect my _children_:
* flex
* grid
* table
* list-item

__inline__ qualities:
- Flows along with the text around it.
- No concept of width or height.
- Ignores the box model.

__<block>__ qualities:
- Creates a clean break before and after.
- Allows you to set the width and height.
- Honors the box model.

The _box model_ provides aesthetic space. This includes __margins__ & __padding__.

There are many units of measurement:
* Pixels __px__
* Ems __em__
* Percentages __%__
* Viewport size __vh__ & __vw__

__%__ & __px__ are best for _screen layout_. __ems__ are for _text_!

## Centering

### Horizontal Centering

__text-align: center;__ only works on _inline_ elements and _NOT block_ elements.

__margin: 0px auto;__ for block elements and _not_ inline, the auto means make it the same on both sides, 

### Vertical Centering

__vertical-align: top;__ applies to the element _inside_. The one you want centered, not on the parent. It only works one a <p> if it is _dispaly:inline-block;_.

The position style has discrete values:
* static: Default value which makes the elements on the page flow nicely. Inline elements live _side-by-side_ as wide as the container allows, then they go down to the next line.
* relative: Participates in the layout of the page as normal, but then is moved _relative_ to where it would have been. Positioned relative to its first positioned parent.
* absolute: Takes it out of the document flow. Positions it _absolutely_ on the page.
* fixed: Will be _fixed_ to a spot in the browser and __not__ the page. Ignores everything else on the page. 

# Page Layout Strategy

Pages have differentsections which require some planning to lay them out nicely. 

Three good tips on how to achieve this goal are:
1. Define sections
2. Define sizes
3. Get them to live side-by-side

You can do this by preferably using _inline sections_, but you could also use _tables_ or _absolute positioning_, although these are discouraged.

You'll want to have a hybrid of __inline__ and __block__ elements, such as the following: 
- floated divs
- display: inline-block
- flex boxes
- grids

A __floated__ element allows things below it to float up next to it- __IF THERE IS ROOM__.

__clear__ allows for the last item to be dropped below the floated elements.

__display: inline-block__ honors width like a block, and allows side-by-side like an inline. However, alignment and spacing are issues because they're vertically aligned at the bottom and there's a space between sections even with no margin. :(

__flexbox__ lays out either across or down but not both. If there are too many items, you can wrap it down to the next line, and if you don't then you can decide how to allocate the extra space.

__grid__ is basically a cleaner _table_.

# Layouts with Flexbox



# Layouts with Grid

__grids__ allow us to lay out pages in grids and columns by assigning lines between them to create the cells. You can even combine the cells to create sections and assign items to the sections. 

_containers_ have _items_, containers have _lines_ that define the rows and columns, _cells_ are where the tracks intersect, cells can be combined into rectangular _areas_.

A __container__ can be ANYTHING in your document.

__fr__ is _free space_. This is better than __%__ because it takes into account grid gaps. 

__grids__ will ONLY and ALWAYS place it's direct children. Just like __flexbox__.

We usually want to let heights be changed based on the content. Do this by specifying _auto_ for the height of the row. 

 
# How do I make this layout?

There is more than one way to create your webpage, but you want to make sure it not only looks good, but is also well constructed. 

(We did a bunch of examples in class on what layout we think would best suite the screens given)

# Progressive Web Apps & Responsive Design

__PWAs__ have tons of requirements, but they allow for offline use. So it is very useful. This is where __Media Queries__ come in. They rely on responsive web designs that flex when browsed on many devices.

__PWAs__:
* Must be served over HTTPS
* Run offline
* Can have an icon on the home screen

Some people add even more requirements:
* Responsive
* Loads instantly (funny)
* Asks the user to add to home screen
* Push notifications
* Runs fast even on slow networks
* Cross-browser
* Page transitions are fast
* Each page gets its own URL

There are many other applications for web apps, not just shopping. Many businesses run their platforms in some type of mobile way.

We want to create an experience that convinces the user that they are online when they are actually not. Use local storages, re-syncing, and try to keep the activity as legit as possible while offline.


You can use the _media_ attribute, to allow for many screen readers to be able to view your content easily. 

# Modern CSS

CSS styles give the look and feel by setting colors, fonts, sizes, and other graphical features.

There are __16,777,216__ colors availble in the RGB range.

Web fonts allow you to expand beyond the installed fonts. You can use them as long as they are free :grinning:.

Data uris _may_ speed up your images, but use caution!

# Advanced CSS Selectors

CSS __selectors__ allow us great flexibility in pointing to elements on a page. 
We can point to these elements by id, class, and type, but they go much deeper as in position, attributes, state, and more,

Class selectors allow you to group elements any way you see fit. 

You can also _concatenate_ them!

A comma means you're applying a style to two or more selectors.

## Relationship Selectors

The __DOM__ also points to the relationships between elements. You are able to select descendants as well asn direct children.

## Pseudo-classes

Denoted with a _:_, these are similar, but not actually classes from css. Examples of these are:
* :link
* :visited
* :hover
* :active
* :focus
and many, many more.

## Pseudo-elements

Denoted with a _::_, these point to otherwise inaccessible parts of the page. The __::before__ & __::after__ selectors allow you to insert content _inside_  an element. 

# CSS Transforms and Transitions

Transforms can make our sites come alive with translate, scale, rotate, and more. The transition features allows us to create smooth transforms with control over duration, intial delay, and the easing function,

This allows us to drastically reduce the size of our programs and they are more robust that way.

The __timing__ function tells how the transition _accelerates_ over time.

The __delay__ tells how long to wait before the beginning.

# Tables

HTML tables are for __data__, not __layout__. They can have their own headers and footers, as well as they span rows and columns.

# Best Practices with Forms

Forms are used to collect data from the user and then send them to a server for processing. A few of these forms are:
* textarea: These are for _multiline_ items in forms
* select: These are for _listboxes_ or _dropdowns_
* datalist: These are for _everything else_

There are lots of <input> fields with types like:
* text
* search
* number
* range
* email

The __form__ tag posts their data in the __POST__ request's payload.


