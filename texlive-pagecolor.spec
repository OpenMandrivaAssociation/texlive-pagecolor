# revision 25500
# category Package
# catalog-ctan /macros/latex/contrib/pagecolor
# catalog-date 2014-02-26 23:03:13 +0100
# catalog-license lppl
# catalog-version 1.0e
Name:		texlive-pagecolor
Version:	1.0e
Release:	10
Summary:	Interrogate page colour
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/pagecolor
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pagecolor.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pagecolor.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pagecolor.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides the command \thepagecolor, which gives
the current page (background) colour, i. e. the argument used
with the most recent call of \pagecolor{...}. The command
\thepagecolornone gives the same colour as \thepagecolor,
except when the page background colour is "none" (e.g., as a
result of using the \nopagecolor command). In that case
\thepagecolor is "white" and \thepagecolornone is "none".

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/pagecolor/pagecolor.sty
%doc %{_texmfdistdir}/doc/latex/pagecolor/README
%doc %{_texmfdistdir}/doc/latex/pagecolor/pagecolor-example.pdf
%doc %{_texmfdistdir}/doc/latex/pagecolor/pagecolor-example.tex
%doc %{_texmfdistdir}/doc/latex/pagecolor/pagecolor.pdf
#- source
%doc %{_texmfdistdir}/source/latex/pagecolor/pagecolor.drv
%doc %{_texmfdistdir}/source/latex/pagecolor/pagecolor.dtx
%doc %{_texmfdistdir}/source/latex/pagecolor/pagecolor.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
