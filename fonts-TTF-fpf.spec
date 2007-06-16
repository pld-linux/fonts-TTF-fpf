%define		subver	Beta-1
Summary:	Free Persian fonts
Summary(pl.UTF-8):	Darmowe czcionki perskie
Name:		fonts-TTF-fpf
Version:	1.0.0
Release:	1
License:	GPL
Group:		Fonts
Source0:	http://dl.sourceforge.net/fpf/fpf-%{version}-%{subver}.tar.gz
# Source0-md5:	5bb2f3aea3c3a43119d72cac0bfc7f11
URL:		http://fpf.sourceforge.net/per/index.html
Requires(post,postun):	fontpostinst
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		ttffontsdir	%{_fontsdir}/TTF

%description
This package contains free fonts of Persian (Farsi) alphabet.

%description -l pl.UTF-8
Ten pakiet zawiera czcionki alfabetu perskiego (Farsi).

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{ttffontsdir}

install FreePersianFont/*.ttf $RPM_BUILD_ROOT%{ttffontsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst TTF

%postun
fontpostinst TTF

%files
%defattr(644,root,root,755)
%doc FreePersianFont/{README,Changelog}
%{ttffontsdir}/*.ttf
