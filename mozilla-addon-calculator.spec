
%define         _prefix         /usr/X11R6
%define         _chromedir      %{_libdir}/mozilla/chrome
%define		_realname	mozcalc

Summary:        Calculator for Mozilla
Summary(pl):    Kalkulator dla Mozilli
Name:           mozilla-addon-calculator
Version:        0.4.0
Release:        2
License:        LGPL
Group:          X11/Applications/Networking
Source0:	http://mozcalc.mozdev.org/mozcalc-0.4.0.xpi
Source1:        %{_realname}-installed-chrome.txt
URL:            http://mozcalc.mozdev.org/
BuildRequires:  unzip
Requires:       mozilla >= 1.0
BuildRoot:      %{tmpdir}/%{_realname}-%{version}-root-%(id -u -n)



%description
%description -l pl
Kalkulator naukowy z odwrotn± notacj± polsk±, w pe³ni zintegrowany z
mozill±.

%prep
%setup -q -c -T
%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_chromedir}
unzip %{SOURCE0} -d $RPM_BUILD_ROOT%{_chromedir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_chromedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
cd %{_chromedir}
cat %{_realname}-installed-chrome.txt >> installed-chrome.txt

%postun
cd %{_chromedir}
cat installed-chrome.txt |grep -v "%{_realname}" > installed-chrome.txt.tmp
cat installed-chrome.txt.tmp > installed-chrome.txt
rm -f installed-chrome.txt.tmp

%files
%defattr(644,root,root,755)
%{_chromedir}/%{_realname}.jar
%{_chromedir}/%{_realname}-installed-chrome.txt
