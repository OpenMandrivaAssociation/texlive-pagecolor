# revision 23556
# category Package
# catalog-ctan /macros/latex/contrib/pagecolor
# catalog-date 2011-08-12 11:32:52 +0200
# catalog-license lppl
# catalog-version 1.0c
Name:		texlive-pagecolor
Version:	1.0c
Release:	1
Summary:	Interrogate page colour
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/pagecolor
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pagecolor.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pagecolor.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pagecolor.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
This package provides the command \thepagecolor, which gives
the current page (background) colour, i. e. the argument used
with the most recent call of \pagecolor{...}. The command
\thepagecolornone gives the same colour as \thepagecolor,
except when the page background colour is "none" (e.g., as a
result of using the \nopagecolor command). In that case
\thepagecolor is "white" and \thepagecolornone is "none".

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
