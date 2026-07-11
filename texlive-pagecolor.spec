%global tl_name pagecolor
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.2d
Release:	%{tl_revision}.1
Summary:	Interrogate page color
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/pagecolor
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pagecolor.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pagecolor.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pagecolor.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides the command \thepagecolor, which gives the current
page (background) color, i. e. the argument used with the most recent
call of \pagecolor{...}. The command \thepagecolornone gives the same
color as \thepagecolor, except when the page background color is "none"
(e.g., as a result of using the \nopagecolor command). In that case
\thepagecolor is "white" and \thepagecolornone is "none". When
\nopagecolor is unknown or broken (crop package), this package provides
a replacement. Similar to \newgeometry and \restoregeometry of the
geometry package \newpagecolor{...} and \restorepagecolor are provided.
For use with the crop package \backgroundpagecolor{...} as well as
\newbackgroundpagecolor{...} and \restorebackgroundpagecolor are
provided.

