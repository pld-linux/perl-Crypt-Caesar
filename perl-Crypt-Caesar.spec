%include	/usr/lib/rpm/macros.perl
%define		pdir	Crypt
%define		pnam	Caesar
Summary:	Crypt::Caesar Perl module - decrypt rot-N strings
Summary(pl):	Modu³ Perla Crypt::Caesar - odszyfrowuj±cy ci±gi znaków w rot-N
Name:		perl-Crypt-Caesar
Version:	0.01
Release:	2
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	f0a7773261b15920312d763a31c630d7
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module is based on the caesar program from the bsd-games package,
made by Stan King and John Eldridge, based on the algorithm suggested
by Bob Morris.
	    
%description -l pl
Ten modu³ bazuje ma programie caesar z pakietu bsd-games, napisanym
przez Stana Kinga i Johna Eldridge'a, bazuj±c na algorytmie
zasugerowanym przez Boba Morrisa.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Crypt/Caesar.pm
%{_mandir}/man3/*
