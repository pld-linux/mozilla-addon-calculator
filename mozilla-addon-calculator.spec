Summary:	Calculator for Mozilla
Summary(pl):	Kalkulator dla Mozilli
Name:		mozilla-addon-calculator
%define		_realname	mozcalc
Version:	0.4.0
Release:	5
License:	LGPL
Group:		X11/Applications/Networking
Source0:	http://mozcalc.mozdev.org/%{_realname}-%{version}.xpi
# Source0-md5:	4d4ab8cf0a9caa0774fabfd31e5b3860
Source1:	%{_realname}-installed-chrome.txt
URL:		http://mozcalc.mozdev.org/
BuildRequires:	unzip
Requires(post,postun):	mozilla >= 1.7.3-3
Requires(post,postun):	textutils
Requires:	mozilla >= 1.0-7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{_realname}-%{version}-root-%(id -u -n)

%define		_chromedir	%{_datadir}/mozilla/chrome

%description
This is scientific calculator which supports Reverse Polish Notation.
It's fully integrated with Mozilla.

%description -l pl
Kalkulator naukowy z odwrotn± notacj± polsk±, w pe³ni zintegrowany z
Mozill±.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_chromedir}

unzip %{SOURCE0} -d $RPM_BUILD_ROOT%{_chromedir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_chromedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{_sbindir}/mozilla-chrome+xpcom-generate

%postun
%{_sbindir}/mozilla-chrome+xpcom-generate

%files
%defattr(644,root,root,755)
%{_chromedir}/%{_realname}.jar
%{_chromedir}/%{_realname}-installed-chrome.txt
