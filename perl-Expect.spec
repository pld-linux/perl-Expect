%include	/usr/lib/rpm/macros.perl
Summary:	Expect perl module
Summary(pl):	Modu³ perla Expect
Name:		perl-Expect
Version:	1.11
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Expect/Expect-%{version}.tar.gz
Patch0:		%{name}-paths.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRequires:	perl-IO-Stty
BuildRequires:	perl-IO-Tty
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Expect perl module.

%description -l pl
Modu³ perla Expect.

%prep
%setup -q -n Expect-%{version}
%patch -p1

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes README FAQ.old

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz tutorial
%{perl_sitelib}/Expect.pm
%{_mandir}/man3/*
