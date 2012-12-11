%define build_with_tests	1

%define name	primer3
%define version 2.3.1
%define release 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	PCR reactions primers identification
Group:		Sciences/Biology
License:	BSD and GPLv2+
URL:		http://primer3.sourceforge.net/
Source0:	http://downloads.sourceforge.net/primer3/%{name}-%{version}.tar.gz
Patch0:		primer3-2.2.3-linking.patch

%description
Primer3 is a complete rewrite of the original PRIMER program
(Primer 0.5), written by Steve Lincoln, Mark Daly, and Eric
Lander.

Primer3 picks primers for PCR reactions, considering as criteria:
- oligonucleotide melting temperature, size, GC content,
  and primer-dimer possibilities
- PCR product size
- positional constraints within the source sequence
- miscellaneous other constraints

All of these criteria are user-specifiable as constraints, and
some are specifiable as terms in an objective function that
characterizes an optimal primer pair.

%prep
%setup -q -n %{name}-%{version}
%patch0  -p1 -b .linking

%build
%make -C src CFLAGS="%{optflags} -D__USE_FIXED_PROTOTYPES__" LDFLAGS="%{ldflags}" V=1 

%install
install -Dpm 755 src/primer3_core %{buildroot}%{_bindir}/primer3_core
install -Dpm 755 src/ntdpal %{buildroot}%{_bindir}/ntdpal
install -Dpm 755 src/ntthal %{buildroot}%{_bindir}/ntthal
install -Dpm 755 src/oligotm %{buildroot}%{_bindir}/oligotm
install -Dpm 755 src/long_seq_tm_test %{buildroot}%{_bindir}/long_seq_tm_test

%if %build_with_tests
%check
%make -C test
%endif

%files
%doc *.txt *.htm example src/release_notes.txt
%{_bindir}/*


%changelog
* Fri Jul 20 2012 Alexander Khrukin <akhrukin@mandriva.org> 2.3.1-1
+ Revision: 810411
- version update 2.3.1

* Tue Feb 28 2012 Alexander Khrukin <akhrukin@mandriva.org> 2.3.0-1
+ Revision: 781276
- version update 2.3.0

* Fri Dec 10 2010 Jani Välimaa <wally@mandriva.org> 2.2.3-1mdv2011.0
+ Revision: 620447
- new version 2.2.3
- enable build time tests

* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 1.1.4-3mdv2011.0
+ Revision: 614611
- the mass rebuild of 2010.1 packages

* Mon Mar 15 2010 Eric Fernandez <zeb@mandriva.org> 1.1.4-2mdv2010.1
+ Revision: 519887
- rebuild

* Tue Aug 18 2009 Eric Fernandez <zeb@mandriva.org> 1.1.4-1mdv2010.0
+ Revision: 417799
- added 1.1.4 source
- removed old version source
- version 1.1.4 and fix format arguments patch

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 1.1.1-3mdv2009.0
+ Revision: 242331
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Mon Aug 06 2007 Eric Fernandez <zeb@mandriva.org> 1.1.1-1mdv2008.0
+ Revision: 59287
- update version 1.1.1

