Summary:	Calculator for Mozilla
Summary(pl):	Kalkulator dla Mozilli
Name:		mozilla-addon-calculator
%define		_realname	mozcalc
Version:	0.4.0
Release:	3
License:	LGPL
Group:		X11/Applications/Networking
Source0:	http://mozcalc.mozdev.org/%{_realname}-%{version}.xpi
Source1:	%{_realname}-installed-chrome.txt
URL:		http://mozcalc.mozdev.org/
BuildRequires:	unzip
BuildArch:	noarch
Requires:	mozilla >= 1.0-7
BuildRoot:	%{tmpdir}/%{_realname}-%{version}-root-%(id -u -n)

%define         _prefix         /usr/X11R6
%define         _chromedir      %{_libdir}/mozilla/chrome

%description
This is scientific calculator which supports Reverse Polish Notation.
It's fully integrated with Mozilla.

%description -l pl
Kalkulator naukowy z odwrotn� notacj� polsk�, w pe�ni zintegrowany z
Mozill�.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_chromedir}

unzip %{SOURCE0} -d $RPM_BUILD_ROOT%{_chromedir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_chromedir}

%post
cat %{_chromedir}/*-installed-chrome.txt >%{_chromedir}/installed-chrome.txt

%postun
cat %{_chromedir}/*-installed-chrome.txt >%{_chromedir}/installed-chrome.txt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_chromedir}/%{_realname}.jar
%{_chromedir}/%{_realname}-installed-chrome.txt
